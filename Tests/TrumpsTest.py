import unittest
import src.Trumps


class TrumpsTest(unittest.TestCase):

    def test_getPlayerName(self):
        trueArray = ["Daniel", "Mark"]
        result = src.Trumps.getName()
        self.assertIn(result, trueArray)

    def test_notFraser(self):
        result = src.Trumps.getName()
        self.assertEqual("Not Today Fraser", result)

    def test_trumpSuit(self):
        result = src.Trumps.gettrumpSuit()
        self.assertIn(result, ["C", "D", "H", "S"])

    def test_leaderboard(self):
        import os.path
        from os import path
        self.assertTrue(path.exists("Leaderboard.txt"))

    def test_playGame(self):
        result = src.Trumps.playGame([["C5", "C8", "D8", "DK", "HJ", "HQ", "HA"]], "Mark")
        self.assertEqual(SystemExit, result)

