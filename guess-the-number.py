from random import randint

randomNumber = randint(1,4)

numberGuessed = int(input("Please Guess your number"))

if(numberGuessed == randomNumber):
    print("Win")
else:
    print("You Lost")