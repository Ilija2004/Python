##import random

from random import randint

guess = randint(1,6)
print(guess)


lives = 0

while lives < 3:
    userIn = int(input("Please input a random number between 1 and 6 : "))

    if  userIn == guess:
        print("You guessed the number")
        exit()
    

    else :
        print("You are wrong")
        lives += 1
        if lives == 3:
            print("Game Over ! - The number was",guess)
        

    
    
    

