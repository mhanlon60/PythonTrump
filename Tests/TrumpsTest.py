import unittest
import src.Trumps


class TrumpsTest(unittest.TestCase):

    def test_getAccuratePlayerName(self):
        trueArray = ["daniel", "mark"]
        result = src.Trumps.getName("mark").lower()
        self.assertIn(result, trueArray)

    def test_trumpSuit(self):
        result = src.Trumps.gettrumpSuit()
        self.assertIn(result, ["C", "D", "H", "S"])

    def test_leaderboard(self):
        import os.path
        from os import path
        self.assertTrue(path.exists("Leaderboard.txt"))

    def test_playerCardsValue(self):
        result = src.Trumps.cardsValue1("CK")
        self.assertEqual(1002,result)

    def test_opponentCardsValue(self):
        result = src.Trumps.cardsValue2("DQ")
        self.assertEqual(1001,result)

    def test_CardValueOf10(self):
        result = src.Trumps.cardsValue1("H10")
        self.assertEqual(999,result)



