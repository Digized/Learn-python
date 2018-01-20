import random

def chosenValue(playAgain):
    if(playAgain == "yes"):
        return "yes"
    elif(playAgain == "no"):
        return "no"
    else:
        playAgain = input("Please Try Again\n")
        return chosenValue(playAgain)


playAgain = input("Do you want to play?\n")
playAgain = chosenValue(playAgain)
while(playAgain == "yes" and playAgain != "no"):
    a = int(input("What is minimum number: "))
    b = int(input("What is the maximum number: "))
    randomGen = random.randint(a, b)
    print("Dice rolled a", randomGen)
    playAgain = input("Do you want to play again?\n")
    playAgain = chosenValue(playAgain)





