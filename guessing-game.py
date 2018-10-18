#Ashley Wohlrab
#Lab Activity #5

answer = "dolphin"

def userInput():
        givenInput = input("Computer is thinking of an animal...").lower()
        return givenInput

def likeAnimal():
    Input = input("Do you like this animal?").lower()
    return Input

def startsWith():
    x= 'quit'

def askQuestion():
    Game = True
    while Game:
        Input = likeAnimal()
        if Input == "yes":
            print("I do too! Cool!")
            break
        elif Input == "no":
            print("I'm sorry to hear that!")
            break
        elif Input[0]=='q':
            break
        else:
            print("Please respond with Yes or No")
        


def guessingGame():
    Game = True
    while Game:
        input = userInput()
        if input == "dolphin": 
            print("You have guessed the correct animal! Congratulations!")
            askQuestion()
            break
        elif input[0]=='q':
            break
        else:
            print("That is not the correct animal. Please try again.")
    


def main():
    print("PYTHON GUESSING GAME.")
    guessingGame()
    
main()



        
        

    
