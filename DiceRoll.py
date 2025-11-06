import random

def diceRoll():
    diceValue = random.randint(1,6)
    return diceValue

def startGame():
    print("Welcome to Dice game! Its its your roll vs. theirs")
    print("this code is live on github")
    ourRoll = diceRoll()
    theirRoll = diceRoll()
    print("you rolled a " + str(ourRoll))
    print("you opponent rolled a " + str(theirRoll))
    if ourRoll == theirRoll:
        print("tie")
    elif ourRoll > theirRoll:
        print("you win")
    else:
        print("you lose")

startGame()
