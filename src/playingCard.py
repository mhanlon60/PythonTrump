import random

suits = {"H": "Hearts", "D": "Diamonds", "S": "Spades", "C": "Clubs"}
faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def generateDeck():
        deck = []
        for suit in suits.keys():
            for face in faces:
                deck.append(suit + face)
        return deck


def dealACard(cards):
    return cards.pop()



def dealCards(deck,noOfCards,noOfHands):
    hands=[]
    allCards = False
    if noOfCards == 0:
        noOfCards = int(len(deck)/noOfHands) - 1
        allCards = True

    for index in range(0,noOfHands):
        hands += [[]]

    for handIndex in range(0,noOfHands):
        while len(hands[handIndex]) < noOfCards and len(deck) > 0:
            dealtCard = dealACard(deck)
            hands[handIndex].append(dealtCard)

    if allCards:
        counter = 0
        while len(deck) > 0:
            hands[counter].append(dealACard(deck))
            counter = (counter +1) % noOfHands

    return hands

def shuffleCards(cards):
    random.shuffle(cards)
    return cards

def playACard(hand,cardToPlay):
    if cardToPlay in hand:
        hand.remove(cardToPlay)