# CMPT 120 - Lab #6
# Ashley Wohlrab
# 25 October 2018
###

def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', 'exp', and 'quit'.\n")

def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")

def addFunc():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return num1+num2

def subFunct():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return num1-num2

def multFunc():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return num1*num2

def divFunc():
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            num1//num2
        except:
            print("Cannot divide by zero!")
            continue
        return num1//num2

def powerFunc():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return num1**num2
    
def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ").lower()
        
        if cmd == "add":
            x = addFunc()
        elif cmd == "sub":
            x = subFunc()
        elif cmd == "mult":
            x = multFunc()
        elif cmd == "div":
            x = divFunc()
        elif cmd == "exp":
            x = powerFunc()
        elif cmd == "quit":
            break   
        else:
            print("That is not a valid command.")
            continue
    
        print("The result is " + str(x) + ".\n")

def main():
    showIntro()
    doLoop()
    showOutro()

main()
