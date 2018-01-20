import random

playAgain = input("Do you want to play?\n")
while( playAgain == "yes"):
    a = int(input("What is minimum number: "))
    b = int(input("What is the maximum number: "))
    randomGen = random.randint(a, b)
    print("Dice rolled a", randomGen)
    playAgain = input("Do you want to play again?\n")