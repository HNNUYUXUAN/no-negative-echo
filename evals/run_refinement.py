"""Run native Codex regression tasks in new workspaces; results are not auto-graded."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]


def observed_modules(parsed):
    """Count module text returned by successful shell or MCP calls, not requests."""
    modules = set()
    for event in parsed:
        if event.get('type') != 'item.completed':
            continue
        item = event.get('item', {})
        output = ''
        if item.get('type') == 'command_execution' and item.get('exit_code') == 0:
            output = item.get('aggregated_output', '')
        elif item.get('type') == 'mcp_tool_call' and not item.get('error'):
            result = item.get('result') or {}
            if not result.get('isError'):
                output = '\n'.join(p.get('text', '') for p in result.get('content', [])
                                   if p.get('type') == 'text')
        modules.update(key for key in ('EX-1', 'CO-1', 'PC-1', 'EN-1') if key in output)
    return sorted(modules)


def run_case(case, workspace, installed=False):
    folder = workspace / case['id']
    folder.mkdir()  # Preserve existing runs; choose a fresh workspace to repeat.
    subprocess.run(['git', 'init', '-q', str(folder)], check=True)
    user_skill = Path.home() / '.agents/skills/no-negative-echo'
    if installed:
        skill = user_skill
    else:
        skill = folder / '.agents/skills/no-negative-echo'
        shutil.copytree(ROOT / 'no-negative-echo', skill,
                        ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    expected = (skill / 'SKILL.md').read_text(encoding='utf-8').strip()
    for name, text in case.get('files', {}).items():
        (folder / name).write_bytes(text.encode('utf-8'))
    prompt = '$no-negative-echo\n\n' + case['prompt']
    (folder / 'input.txt').write_bytes(prompt.encode('utf-8'))
    cli = shutil.which('codex')
    if not cli:
        raise RuntimeError('Codex CLI is required')
    args = [cli, 'exec', '--skip-git-repo-check', '-C', str(folder), '-s', 'workspace-write',
            '--json', '-o', str(folder / 'answer.txt')]
    if installed:
        args += ['--add-dir', str(skill)]
    if not installed:
        # Command-local override; the user's configuration file is unchanged.
        args += ['-c', 'skills.config=[{path=' + json.dumps((user_skill / 'SKILL.md').as_posix())
                 + ',enabled=false}]']
    args += ['-']
    start = time.time()
    with (folder / 'events.jsonl').open('w', encoding='utf-8') as events, \
         (folder / 'stderr.txt').open('w', encoding='utf-8') as errors:
        try:
            process = subprocess.run(args, cwd=folder, input=prompt, text=True,
                                     encoding='utf-8', stdout=events, stderr=errors, timeout=360)
            code = process.returncode
        except subprocess.TimeoutExpired:
            code = 'timeout'
    parsed = []
    for line in (folder / 'events.jsonl').read_text(encoding='utf-8').splitlines():
        try:
            parsed.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    session = next((e.get('thread_id') for e in parsed if e.get('type') == 'thread.started'), None)
    native = False
    models = set()
    if session:
        home = Path(__import__('os').environ.get('CODEX_HOME', str(Path.home() / '.codex')))
        for path in (home / 'sessions').rglob('*' + session + '*.jsonl'):
            for line in path.read_text(encoding='utf-8').splitlines():
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    continue
                payload = event.get('payload', {})
                if event.get('type') == 'turn_context' and payload.get('model'):
                    models.add(payload['model'])
                if (event.get('type') == 'response_item' and payload.get('type') == 'message'
                        and payload.get('role') == 'user'):
                    native |= any(expected in part.get('text', '') for part in payload.get('content', []))
    messages = []
    exits = []
    for event in parsed:
        if event.get('type') != 'item.completed':
            continue
        item = event['item']
        if item['type'] == 'agent_message':
            messages.append(item['text'])
        if item['type'] == 'command_execution':
            exits.append(item.get('exit_code'))
    def clean(text):
        return text.replace(str(folder), '<task>').replace(folder.as_posix(), '<task>')
    return {
        'id': case['id'], 'exit_code': code, 'seconds': round(time.time() - start, 1),
        'models': sorted(models), 'native_entry_matches_candidate': native,
        'version': json.loads((skill / 'delivery.json').read_text(encoding='utf-8'))['version'],
        'provenance_sha256': hashlib.sha256((skill / '.no-negative-echo-provenance.json').read_bytes()).hexdigest(),
        'skill_sha256': hashlib.sha256((skill / 'SKILL.md').read_bytes()).hexdigest(),
        'modules_read': observed_modules(parsed), 'command_exit_codes': exits,
        'messages': [clean(m) for m in messages],
        'answer': clean((folder / 'answer.txt').read_text(encoding='utf-8')) if (folder / 'answer.txt').exists() else None,
        'artifacts': {name: (folder / name).read_text(encoding='utf-8')
                      for name in case.get('artifacts', []) if (folder / name).exists()},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, required=True)
    parser.add_argument('--only', nargs='+')
    parser.add_argument('--installed', action='store_true')
    args = parser.parse_args()
    workspace = args.workspace.resolve()
    if workspace == ROOT or ROOT in workspace.parents:
        parser.error('Use a workspace outside the repository')
    workspace.mkdir(parents=True, exist_ok=True)
    result_path = workspace / 'results.json'
    results = json.loads(result_path.read_text(encoding='utf-8')) if result_path.exists() else []
    cases = json.loads((ROOT / 'evals/refinement-cases.json').read_text(encoding='utf-8'))
    for case in cases:
        if args.only and case['id'] not in args.only:
            continue
        result = run_case(case, workspace, args.installed)
        results.append(result)
        result_path.write_bytes((json.dumps(results, ensure_ascii=False, indent=2) + '\n').encode())
        print(json.dumps(result, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
