import unittest
import src.Trumps


class TrumpsTest(unittest.TestCase):

    def test_getAccuratePlayerName(self):
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

    def test_QuitAfterPlaying(self):
          with self.assertRaises(SystemExit) as cm:
              src.Trumps.playGame([["C5", "C8", "D8", "DK", "HJ", "HQ", "HA"]],
                                  [["C2", "C6", "D2", "DQ", "H2", "H10", "HK"]], "Mark", "H")

          self.assertEqual(cm.exception.code, None)

    def test_playerCardsValue(self):
        result = src.Trumps.cardsValue1("CK")
        self.assertEqual(1002,result)

    def test_opponentCardsValue(self):
        result = src.Trumps.cardsValue2("DQ")
        self.assertEqual(1001,result)

    def test_CardValueOf10(self):
        result = src.Trumps.cardsValue1("H10")
        self.assertEqual(999,result)



