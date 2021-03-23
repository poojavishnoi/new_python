#print logo
#random account
#display the account
#ask to make a guess
#if guess is correct then keep account
#score keeping
#repeatable
#if correct replace A by B and B by next account
#clear


from art import logo
from art import vs
from game_data import data
import random
from replit import clear

def account_details(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_desc}, from {account_country}\n"

def comparision(guess, a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        return guess == "a"
    else:
        return guess == "b"    
print(logo)
score = 0
game_continue = True
account2 = random.choice(data)
while game_continue:
    
    account1 = account2
    account2 = random.choice(data)
    while account1 == account2:
        account2 = random.choice(data)

    
    print(f"Compare A: {account_details(account1)}")

    print(vs+ "\n\n")

    print(f"Against B: {account_details(account2)}")

    guess = input("Who has more followers? Type 'A' OR 'B'\n").lower()
    a_follower_count = account1["follower_count"]
    b_follower_count = account2["follower_count"]

    is_correct = comparision(guess, a_follower_count, b_follower_count)
    clear()
    print(logo)
    if is_correct:
        score += 1
        print(f"You are right. Current score {score}")


    else: 
        print(f"You are wrong. Final score {score}")
        game_continue = False
        