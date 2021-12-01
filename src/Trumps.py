

class Trumps:
    def getName(self):
        playerName = input("Please enter your name : ")


        if playerName.lower() != "fraser":
            return playerName

        message = "Not Today Fraser"
        return message

