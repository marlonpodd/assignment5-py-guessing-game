#Assignment #5
#Marlon
#Guessing Game.py

import random

number = random.randint(1, 99)

guesses = 0

print("You have 5 guesses to find the number")

while guesses < 5:
    guess = int(input("Enter an integer from 1 to 99: "))
    guesses +=1
    print("You have ", 5 - guesses, " guesses left.")
    if guess < number:
        print ("Guess is low")
    elif guess > number:
        print ("Guess is high")
    elif guess == number:
    	break

if guess == number:
    guesses = str(guesses)
    print ("You guess it in : ", guesses + " guesses")

if guess != number:
    number = str(number)
    print ("The secret number was", number)