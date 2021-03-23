#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import random
print(art.logo)
print("Welcome to the Number Guessing Game!!")
print("I'am thinking of a number between 1 to 100.")

random_number = random.randint(1, 100)
#print(random_number)

def easy():
    attempts = 10
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print(f"You got it.The answer is {random_number}")
            break
        elif guess > random_number:
                print("Too high")
        elif guess < random_number:
                print("Too low")
            
        attempts -= 1
    
    print("You lose. Try again")


def hard():
    attempts = 5
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print(f"You got it.The answer is {random_number}")
            break
        elif guess > random_number:
                print("Too high")
        elif guess < random_number:
                print("Too low")
        
            
        attempts -= 1

    print("You lose. Try again")




level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
if level == 'easy':
    easy()
elif level == 'hard':
    hard()



