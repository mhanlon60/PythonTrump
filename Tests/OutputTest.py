import unittest
from unittest.mock import call, patch

import src.Output

class OutputTest(unittest.TestCase):
    @patch('builtins.print')
    def test_printNameToScreen(self, mocked_print):
        src.Output.Output.printToScreen("daniel")
        print()
        assert mocked_print.mock_calls == [call('daniel'), call()]

