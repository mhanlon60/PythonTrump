from src.Input import Input
from src.Output import Output

class getInputInt(Input):

    def getInput(self):
        cardChoice = 0
        try:
            cardChoice = int(input("What Card Do You Want To Play (Enter Card Position)"))
        except ValueError:
            while (not isinstance(cardChoice, int)):
                Output.printToScreen("Error please re-enter your card choice")
                cardChoice = int(input("What Card Do You Want To Play (Enter Card Position)"))

        return cardChoice