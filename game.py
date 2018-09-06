"""A number-guessing game."""

# Put your code here
import random

best_score = None

print("Hi player!")

name = input("What's your name? ")

while  True:

    random_n = random.randrange(1,101)


    choice = input("I picked a number from 1 to 100. Can you guess it? ")


    guesses = 1

    while True:

        while not ((choice.isdigit() == True) and (int(choice)>0) and (int(choice)<101)):
            choice = input("Incorrect input. Pick a number between 1 and 100. ")


        if int(choice) == random_n:
            if best_score == None:
                print("You won! You had {} tries!".format(guesses))
                best_score = guesses
                break
            else:
                if best_score > guesses:
                    best_score = guesses
                print("You won! You had {} tries and your best score is {}!".format(guesses,best_score))
                break

        if int(choice) > random_n:
            choice = input("Too big! Guess again! ")
            guesses+=1
        else:
            choice = input("Too small! Guess again! ")
            guesses+=1


    answer = input("Do you want to play again? (Y/N) ")

    if answer == 'N':
        break
 
