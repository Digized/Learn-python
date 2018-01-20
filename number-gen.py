import random

a = int(input("What is minimum number"))
b = int(input("What is the maximum number"))

randomGen = random.randint(a, b)

print("Dice rolled a", randomGen)

