import art
from replit import clear

#HINT: You can call clear() to clear the output in the console.
print(art.logo)
print("Welcome to the auction bid")
again = True
complete_info = {}
def higest_bidder(bidder_record):
    max = 0
    winner = ""
    for bidder in bidder_record:
        amount = bidder_record[bidder]
        if amount > max:
            max = bidder_record[bidder]
            winner = bidder

    print(f"The highest bid is ${max} by {winner}")

while again:
    bidder_name = input("What is your name:\n")
    bid_price = int(input("Enter the bid price:\n$"))

    complete_info[bidder_name] = bid_price
    repeat = input("Are there any other bidders. Enter 'yes' or 'no'.\n")
    

    if repeat == "no":
        again = False
        higest_bidder(complete_info)
    elif repeat == "yes":
        clear()

