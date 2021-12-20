from src.playingCard import generateDeck, shuffleCards, dealCards
from src.Input import Input
from src.getInputString import getInputString
from src.getInputInt import getInputInt
from src.Output import Output
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

userInput = None

def initDeck():
    deck = generateDeck()
    shuffleCards(deck)
    return deck


deck = initDeck()
# printToScreen(deck)


def getName(testInput = ""):
    if testInput == "":
        setUserInput(getInputString)
        playerName = userInput.getInput()
        return playerName
    else:
        playerName = testInput
        return playerName

def setUserInput(intOrString):
    global userInput
    userInput = intOrString()

def gettrumpSuit():
    trumpSuitArr = ["C", "D", "H", "S"]
    r = (random.randint(0, 3))
    trumpSuit = trumpSuitArr[r]
    Output.printToScreen("Trumps are " + trumpSuit)
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
    setUserInput(getInputInt)
    while Gameplaying:
        while u < len(playerDeck):

            Output.printToScreen(playerDeck)
            #Output.printToScreen(trumpSuit)
        # Output.printToScreen(opponentDeck)

            cardChoice = userInput.getInput()
            Output.printToScreen(cardChoice)

            while (cardChoice > len(playerDeck[0]) or cardChoice < 1):
                Output.printToScreen("Error please re-enter your card choice")
                cardChoice = userInput.getInput()

            chosenCard = playerDeck[0][cardChoice - 1]
            Output.printToScreen("You have chosen " + chosenCard)

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
                            Output.printToScreen("Opponent plays " + opponentCard)
                            foundsameSuit = True

                            if (foundsameSuit == True):
                               ## if ((len(chosenCard) and len(opponentCard)) == 2):
                                    if (cardsValue1(chosenCard) > cardsValue2(opponentCard)):
                                        Output.printToScreen("You win\n")
                                        handswon = handswon + 1
                                    elif (cardsValue1(chosenCard) < cardsValue2(opponentCard)):
                                        Output.printToScreen("You lost\n")
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
                                Output.printToScreen("Opponent plays " + opponentCard)
                                foundtrumpSuit = True

                                if (foundtrumpSuit == True and foundsameSuit == False):
                                    Output.printToScreen("You lose\n")
                                    handslost = handslost + 1

                                Suitvalidated = True
                                break

                            t = t + 1

                        Suitvalidated = True

                    if (foundsameSuit == False and foundtrumpSuit == False):
                        opponentCard = opponentDeck[0][0]
                        Output.printToScreen("Opponent plays " + opponentCard)
                        opponentDeck[0].pop(0)
                        foundnoSuit = True

                        if (foundnoSuit == True):
                            Output.printToScreen("You win\n")
                            handswon = handswon + 1

                        Suitvalidated = True

                if (len(playerDeck[0]) == 0):
                    if (handslost < handswon):
                        Output.printToScreen("You win the game")
                        Gameplaying = False
                        leaderboard(handswon, handslost, playerName)
                    elif (handslost > handswon):
                        Output.printToScreen("You lose the game")
                        Gameplaying = False
                        leaderboard(handswon, handslost, playerName)
                    else:
                        Output.printToScreen("You Draw")
                        Gameplaying = False
                        leaderboard(handswon, handslost, playerName)

            validate(handswon, handslost, playerName, opponentDeck)

def declareMethods():
    deck = initDeck()
    playerDeck = dealPlayerCards(deck)
    #Output.printToScreen(playerDeck)
    opponentDeck = dealOpponentCards(deck)
    #Output.printToScreen(opponentDeck)
    playerName = getName()
    trumpSuit = gettrumpSuit()
    playGame(playerDeck, opponentDeck, playerName, trumpSuit)

def main():
    declareMethods()

if __name__ == "__main__":
    main()