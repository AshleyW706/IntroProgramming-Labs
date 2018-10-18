#Ashley Wohlrab
#Lab Activity #5


def main():
    print("PYTHON GUESSING GAME.")

main()


answer = "dolphin"

def userInput():
        givenInput = input("Computer is thinking of an animal...").lower()
        return givenInput

def guessingGame():
    Game = True
    while Game:
        input = userInput()
        if input == "dolphin": 
            print("You have guessed the correct animal! Congratulations!")
            break
        else:
            print("That is not the correct animal. Please try again.")

guessingGame()
