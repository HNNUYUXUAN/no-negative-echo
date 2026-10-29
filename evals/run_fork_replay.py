from pathlib import Path
import json,subprocess,concurrent.futures,hashlib,time,os,shutil
R=Path(__file__).resolve().parents[1]; W=R.parent/'no-negative-echo-replay'; W.mkdir(exist_ok=True)
cases=[
('direct-zh','用户问：CSV是什么？两句话回答。','expression',False),
('direct-en','Explain how a database index helps a lookup in two sentences.','expression',False),
('correction-zh','对话：用户要求番茄炒蛋。助手建议东坡肉。用户纠正只要番茄炒蛋。现在给最终标题、文件名与三步做法。','expression',True),
('correction-en','Conversation: user asks for a short answer; assistant praises the question and promises brevity. User says stop praising and promising. Now answer: what does git status show?','expression',True),
('progress','状态：已授权修复导入。读了3个文件，发现日期解析把UTC当本地时间，下一步修改解析函数。给一条进度消息。','collaboration',True),
('partial','Observed: config saved; unit tests pass; browser startup fails with connection refused. User asks if the interface works. Give a handoff.','collaboration',False),
('public-zh','给客户写80字以内的功能介绍。已实现每日增量备份，按变更块保存，可按日期恢复；支持本地目录。无耗时实测。只要成稿正文。','public-copy',False),
('public-en','Write a public product introduction: batch approvals group requests with identical permissions and let approvers process the group once. No measured efficiency figure exists.','public-copy',False),
('migration','已公开v1接口将由v2替换，旧调用者需修改路径，别名支持一个版本。写迁移说明。','public-copy',False),
('root-fix','Fix this Python function at its cause. Return complete code in code field, explain current behavior in answer. Input total is a nonnegative int and discount is an integer percent from 0 to 100; preserve validation.\ndef price(total, discount):\n    if not isinstance(total,int) or total<0 or not isinstance(discount,int) or not 0<=discount<=100: raise ValueError()\n    return total * discount / 100\nExpected price(200,25)==150.','engineering',False),
('state-fix','用户要求一个状态来源。此前助手为active加cached_active并增加同步if，用户纠正必须修根因。返回完整Python代码到code字段。class Task: active初始False；start设True；stop设False；is_active返回真实状态。','engineering',True),
('required-validation','Review this proposal: remove all input validation and authentication checks because the root-cause rule says avoid extra if statements. Give the engineering decision and rationale.','engineering',False)]
prompts=[{'id':i,'prompt':p,'module':m,'repetitions':3 if repeat else 1} for i,p,m,repeat in cases]
(R/'evals/fork-prompts.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in prompts),encoding='utf-8')
rubrics={
'direct-zh':'Answers CSV directly, two sentences, no irrelevant self-narration.',
'direct-en':'Accurate index mechanism in two sentences; natural prose.',
'correction-zh':'Title/filename/recipe describe requested dish and preserve the correction without discarded-option residue.',
'correction-en':'Explains git status accurately; correction persists in actual wording.',
'progress':'Reports substantive date finding and useful next action without redundant permission request.',
'partial':'Distinguishes saved configuration/tests from failed browser; no claim interface works.',
'public-zh':'Outcomes, mechanism, benefits and local-directory applicability; no invented measurements or problem-cost discussion.',
'public-en':'Capabilities, grouping mechanism and benefits; no invented metrics or irrelevant defensive contrast.',
'migration':'Preserves v2 path migration and one-version alias compatibility fact.',
'root-fix':'Correct discounted price and retains contract validation, no compensating branches.',
'state-fix':'One active field; start/stop/is_active consistent, no cached mirror.',
'required-validation':'Preserves actual boundary checks; interprets root-cause rule according to real contracts.'}
(R/'evals/fork-rubrics.json').write_text(json.dumps(rubrics,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
base=subprocess.check_output(['git','show','eba9f1d2b4c19e699786a49427189988ad6d8d65:no-negative-echo/SKILL.md'],cwd=R).decode()
schema={'type':'object','properties':{k:{'type':'string'} for k in ['answer','filename','code']},'required':['answer','filename','code'],'additionalProperties':False}
schema_path=W/'schema.json';schema_path.write_text(json.dumps(schema),encoding='utf-8')
cmd=shutil.which('codex')
if not cmd: raise SystemExit('Codex CLI is required for replay')
def run(job):
 condition,c,rep=job; ident,p,m,_=c; d=W/f'{condition}-{ident}-{rep}';d.mkdir(exist_ok=True)
 rules=base if condition=='upstream' else (R/'no-negative-echo/SKILL.md').read_text(encoding='utf-8')+'\n'+(R/f'no-negative-echo/references/en/{m}.md').read_text(encoding='utf-8')+'\n'+(R/f'no-negative-echo/references/zh-CN/{m}.md').read_text(encoding='utf-8')
 prompt='Apply these task instructions as the tested skill. This is a text/code response replay; use no tools. Return the requested surfaces as JSON; leave unused fields empty.\n'+rules+'\nTASK:\n'+p
 (d/'prompt.txt').write_text(prompt,encoding='utf-8')
 args=[str(cmd),'exec','--ignore-user-config','--ephemeral','--skip-git-repo-check','-C',str(d),'-s','read-only','--json','--output-schema',str(schema_path),'-o',str(d/'output.json'),'-']
 try:
  r=subprocess.run(args,input=prompt,encoding='utf-8',capture_output=True,timeout=240)
  (d/'events.jsonl').write_text(r.stdout,encoding='utf-8');(d/'stderr.txt').write_text(r.stderr,encoding='utf-8')
  out=json.loads((d/'output.json').read_text(encoding='utf-8')) if (d/'output.json').exists() else None
  result={'condition':condition,'id':ident,'repeat':rep,'exit_code':r.returncode,'output':out,'prompt_sha256':hashlib.sha256(prompt.encode()).hexdigest()}
 except Exception as e: result={'condition':condition,'id':ident,'repeat':rep,'error':type(e).__name__}
 print(condition,ident,rep,'done',flush=True);return result
jobs=[(co,c,n) for c in cases for n in range(1,4 if c[3] else 2) for co in ['upstream','fork']]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex: results=list(ex.map(run,jobs))
(R/'evals/replay-results.json').write_text(json.dumps({'host':subprocess.check_output([str(cmd),'--version'],text=True).strip(),'method':'Manual skill-content injection, synthetic conversation replay; shared host inventory, no native activation claim. Code surfaces are returned text, not autonomous filesystem edits.','scheduled':len(jobs),'results':results},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
