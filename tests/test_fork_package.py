import hashlib
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'no-negative-echo'

class ForkPackageTests(unittest.TestCase):
    def test_language_routes_and_size_limits(self):
        self.assertLessEqual((SKILL / 'SKILL.md').stat().st_size, 4096)
        for module in ('expression','collaboration','public-copy','engineering'):
            ids=[]
            for lang in ('zh-CN','en'):
                path=SKILL / 'references' / lang / (module+'.md')
                self.assertLessEqual(path.stat().st_size,8192)
                ids.append(re.findall(r'^(?:EX|CO|PC|EN)-\d+',path.read_text(encoding='utf-8'),re.M))
            self.assertEqual(ids[0],ids[1])
            self.assertTrue(ids[0])

    def test_manifest_bytes_and_delivery_inventory(self):
        manifest=json.loads((SKILL/'.no-negative-echo-provenance.json').read_text())
        actual={p.relative_to(SKILL).as_posix() for p in SKILL.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
        self.assertEqual(actual,set(manifest['files'])|{'.no-negative-echo-provenance.json'})
        for name,digest in manifest['files'].items():
            self.assertEqual(hashlib.sha256((SKILL/name).read_bytes()).hexdigest(),digest,name)
        delivery=json.loads((SKILL/'delivery.json').read_text())
        self.assertEqual(set(delivery['files']),set(manifest['files'])-{'delivery.json'})

    def test_preserved_upstream_cases_and_new_rubrics(self):
        cases=[json.loads(x) for x in (ROOT/'evals/evaluation-prompts.jsonl').read_text(encoding='utf-8').splitlines()]
        self.assertEqual(len(cases),16)
        new=[json.loads(x) for x in (ROOT/'evals/fork-prompts.jsonl').read_text(encoding='utf-8').splitlines()]
        rubrics=json.loads((ROOT/'evals/fork-rubrics.json').read_text(encoding='utf-8'))
        self.assertEqual({c['id'] for c in new},set(rubrics))
        self.assertEqual(sum(c['repetitions']*2 for c in new),40)
