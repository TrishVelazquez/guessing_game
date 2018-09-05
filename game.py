"""A number-guessing game."""

# Put your code here
import random

print("Hi player!")

name = input("What's your name? ")

random_n = random.randrange(1,101)

guesses = 1

while True:

    choice = input("I picked a number from 1 to 100. Cat you guess it? ")

    while not(int(choice) in range (1,101)):
        choice = input("Incorrect input. Pick a number between 1 and 100. ")
        
    if int(choice) == random_n:
        print("You won! You had {} tries".format(guesses))
        break

    if int(choice) > random_n:
        choice = input("Too big! Guess again! ")
        guesses+=1
    else:
        choice = input("Too small! Guess again! ")
        guesses+=1
 
