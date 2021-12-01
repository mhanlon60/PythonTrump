import unittest
from src.Trumps import Trumps

class TrumpsTest(unittest.TestCase):
    trumps = Trumps()

    def test_getPlayerName(self):
        trueArray = ["Daniel", "Mark"]
        result = self.trumps.getName()
        self.assertIn(result, trueArray)

    def test_notFraser(self):
        result = self.trumps.getName()
        print(result)
        self.assertEqual("Not Today Fraser", result)