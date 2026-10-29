import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location(
    'refinement_runner', Path(__file__).resolve().parents[1] / 'evals/run_refinement.py')
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


def completed(item):
    return {'type': 'item.completed', 'item': item}


class RefinementEvidenceTests(unittest.TestCase):
    def test_mcp_read_result_is_observed(self):
        event = completed({'type': 'mcp_tool_call', 'error': None,
                           'result': {'content': [{'type': 'text', 'text': 'PC-1 text\nCO-1 text'}]}})
        self.assertEqual(runner.observed_modules([event]), ['CO-1', 'PC-1'])

    def test_request_and_failed_results_are_not_reads(self):
        events = [
            completed({'type': 'mcp_tool_call', 'arguments': {'text': 'PC-1'}, 'result': None}),
            completed({'type': 'mcp_tool_call', 'error': 'failed',
                       'result': {'content': [{'type': 'text', 'text': 'EX-1'}]}}),
            completed({'type': 'command_execution', 'exit_code': 1, 'aggregated_output': 'EN-1'}),
        ]
        self.assertEqual(runner.observed_modules(events), [])

    def test_shell_reads_are_deduplicated(self):
        event = completed({'type': 'command_execution', 'exit_code': 0,
                           'aggregated_output': 'EX-1 text\nEX-1 text'})
        self.assertEqual(runner.observed_modules([event, event]), ['EX-1'])
