from src.playingCard import generateDeck, shuffleCards, dealCards
import random

deck = []
playerDeck = []
opponentDeck = []
startingCards = 7
trumpSuit = ""
u = 0;
endRound = False
trump = False
gameover = False
Gameplaying = True;
handplaying = True;
chosenCard = ""
opponentCard = ""
handswon = 0
handslost = 0


def initDeck():
    deck = generateDeck()
    shuffleCards(deck)
    return deck


deck = initDeck()
# print(deck)

def getName():
    playerName = input("Please enter your name : ")

    if playerName.lower() != "fraser":
        return playerName

    message = "Not Today Fraser"
    return message

def gettrumpSuit():
    trumpSuitArr = ["C", "D", "H", "S"]
    r = (random.randint(0, 3))
    trumpSuit = trumpSuitArr[r]
    print("Trumps are " + trumpSuit)
    return trumpSuit;

def dealPlayerCards(deck):
    playerDeck = dealCards(deck, startingCards, 1)
    playerDeck[0].sort()
    return playerDeck

def dealOpponentCards(deck):
    opponentDeck = dealCards(deck, startingCards, 1)
    opponentDeck[0].sort()
    return opponentDeck

def leaderboard(handswon, handslost, playerName):
    Header = "Player " + " Games"
    line1 = playerName + ": " + str(handswon)
    line2 = "Opponent" + ": " + str(handslost)
    with open('Leaderboard.txt', 'w') as out:
        out.write('{}\n{}\n{}\n'.format(Header, line1, line2))
        userReact = input("End of game! Do you want to play again (Y) or (N)")
        if userReact.lower() == "y":
            main()
        else:
            quit()

def cardsValue1(chosenCard):

    intvalue1 = 0;

    if chosenCard[1] == "J":
        intvalue1 = 1000
    elif chosenCard[1] == "Q":
        intvalue1 = 1001
    elif chosenCard[1] == "K":
        intvalue1 = 1002
    elif chosenCard[1] == "A":
        intvalue1 = 1003
    elif len(chosenCard) == 3:
        intvalue1 = 999
    else:
        intvalue1 = int(chosenCard[1])

    return intvalue1


def cardsValue2(opponentCard):

    intvalue2 = 0;

    if opponentCard[1] == "J":
        intvalue2 = 1000
    elif opponentCard[1] == "Q":
        intvalue2 = 1001
    elif opponentCard[1] == "K":
        intvalue2 = 1002
    elif opponentCard[1] == "A":
        intvalue2 = 1003
    elif len(opponentCard) == 3:
        intvalue2 = 999
    else:
        intvalue2 = int(opponentCard[1])

    return intvalue2


def playGame(playerDeck, opponentDeck, playerName, trumpSuit):
    while Gameplaying:
        while u < len(playerDeck):

            print(playerDeck)
            #print(trumpSuit)
        # print(opponentDeck)

            cardChoice = (input("What card do you want to play"))

            cardChoice = (int)(cardChoice)
            print(cardChoice)

            while (cardChoice > len(playerDeck[0]) or cardChoice < 1):
                cardChoice = (int)(input("Error! What card do you want to play"))

            chosenCard = playerDeck[0][cardChoice - 1]
            print("You have chosen " + chosenCard)

            playerDeck[0].remove(chosenCard)

            def validate(handswon, handslost, playerName, opponentDeck):
                Suitvalidated = False
                foundsameSuit = False
                foundtrumpSuit = False
                foundnoSuit = False

                s = 0;
                t = 0;
                z = 0;

                while (Suitvalidated == False):

                    while (s < len(opponentDeck[0])):
                        if (opponentDeck[0][s][0] == chosenCard[0]):
                            opponentCard = opponentDeck[0][s]
                            opponentDeck[0].pop(s)
                            print("Opponent plays " + opponentCard)
                            foundsameSuit = True

                            if (foundsameSuit == True):
                               ## if ((len(chosenCard) and len(opponentCard)) == 2):
                                    if (cardsValue1(chosenCard) > cardsValue2(opponentCard)):
                                        print("You win\n")
                                        handswon = handswon + 1
                                    elif (cardsValue1(chosenCard) < cardsValue2(opponentCard)):
                                        print("You lost\n")
                                        handslost = handslost + 1
                               ## else:
                                ##    if (len(chosenCard) == 2 and (int(ord(chosenCard[1]))) > int(ord("A"))):
                                  ##      print("You win\n")
                                    ##    handswon = handswon + 1
                                    ##else:
                                      ##  print("You lost\n")
                                        ##handslost = handslost + 1

                            Suitvalidated = True
                            break

                        s = s + 1

                    if (foundsameSuit == False):
                        while (t < len(opponentDeck[0])):
                            if (opponentDeck[0][t][0] == trumpSuit):
                                opponentCard = opponentDeck[0][t]
                                opponentDeck[0].pop(t)
                                print("Opponent plays " + opponentCard)
                                foundtrumpSuit = True

                                if (foundtrumpSuit == True and foundsameSuit == False):
                                    print("You lose\n")
                                    handslost = handslost + 1

                                Suitvalidated = True
                                break

                            t = t + 1

                        Suitvalidated = True

                    if (foundsameSuit == False and foundtrumpSuit == False):
                        opponentCard = opponentDeck[0][0]
                        print("Opponent plays " + opponentCard)
                        opponentDeck[0].pop(0)
                        foundnoSuit = True

                        if (foundnoSuit == True):
                            print("You win\n")
                            handswon = handswon + 1

                        Suitvalidated = True

                if (len(playerDeck[0]) == 0):
                    if (handslost < handswon):
                        print("You win the game")
                        Gameplaying = False
                        leaderboard(handswon, handslost, playerName)
                    elif (handslost > handswon):
                        print("You lose the game")
                        Gameplaying = False
                        leaderboard(handswon, handslost, playerName)
                    else:
                        print("You Draw")
                        Gameplaying = False
                        leaderboard(handswon, handslost, playerName)

            validate(handswon, handslost, playerName, opponentDeck)

def declareMethods():
    deck = initDeck()
    playerDeck = dealPlayerCards(deck)
    #print(playerDeck)
    opponentDeck = dealOpponentCards(deck)
    #print(opponentDeck)
    playerName = getName()
    trumpSuit = gettrumpSuit()
    playGame(playerDeck, opponentDeck, playerName, trumpSuit)

def main():
    declareMethods()

if __name__ == "__main__":
    main()