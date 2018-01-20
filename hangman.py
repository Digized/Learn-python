
def render(fruit, chosenLetters): 
    s = ""
    for letter in fruit:
        print(letter)
        if(letter in chosenLetters):
            s += letter + " "
        else:
            s += "_ "

tries = 10
fruits = "apple"

chosenLetters = []

render(fruits, chosenLetters)

render("apple", chosenLetters)


guess = input("") # a


