import unittest
from src.getInputString import getInputString
from src.getInputInt import getInputInt

class InputTest(unittest.TestCase):

    def test_InputStringReturnsString(self):
        result = getInputString.getInput(self)
        self.assertIsInstance(result,str)

    def test_InputIntReturnsInt(self):
        result = getInputInt.getInput(self)
        self.assertIsInstance(result, int)
