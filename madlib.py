#Intro to Programming
#Author: Ashley Wohlrab
#Date: 10 September 2018
    
def promptForWords():
    global noun, verb, adjective, place
    noun = input("Enter a noun:")
    verb = input("Enter a verb:")
    adjective = input("Enter an adjective:")
    place = input("Enter a place:")

def makeAndPrintSentence():
    print("The " + adjective + " " + noun + " lives alone at " + place + " and " + verb + ".")

def main():
    promptForWords()
    makeAndPrintSentence()

main()
