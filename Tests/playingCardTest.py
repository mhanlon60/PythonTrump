import unittest
import src.playingCard

class playingCardTest(unittest.TestCase):

    deck = ['HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK', 'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK', 'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK', 'CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK']



    def test_createDeck(self):
        result = src.playingCard.generateDeck()
        self.assertEqual(self.deck, result)

    def test_dealingCards(self):
        result = src.playingCard.dealCards(self.deck, 7, 2)
        self.assertEqual(True, (len(result[0][0]) > 0 and len(result[0][1]) > 0))

    def test_properCardsDealt(self):
        result = src.playingCard.dealCards(self.deck, 7, 2)
        self.assertEqual([['CK', 'CQ', 'CJ', 'C10', 'C9', 'C8', 'C7'],['C6', 'C5', 'C4', 'C3', 'C2', 'CA', 'SK']], result)

    def test_shufflin(self):
        ogDeck = src.playingCard.generateDeck()
        result = src.playingCard.shuffleCards(self.deck)
        self.assertEqual(False, result == ogDeck)