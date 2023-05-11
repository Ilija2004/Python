##import random

from random import randint

guess = randint(1,6)

userIn = int(input("Please input a random number between 1 and 6 : "))

while userIn == guess:
    print("You guessed the number")
else:
    print ("You did not guessed the number ")
    print ("The number was",guess)
