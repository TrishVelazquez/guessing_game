"""A number-guessing game."""

# Put your code here
import random

print("Hi player!")

name = input("What's your name? ")

random_n = random.randrange(1,101)

choice = input("I picked a number from 1 to 100. Cat you guess it? ")

guesses = 1

while True:
    if int(choice) == random_n:
        print("You won! You had {} tries".format(guesses))
        break

    if int(choice) != random_n:
        choice = input("Guess again! ")


