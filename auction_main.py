import os
from art import logo

def bidding(bid):
    max_cost = 0
    winner = ""
    for name in bid:
        user_cost = bid[name]
        if max_cost < user_cost:
            max_cost = user_cost
            winner = name
    print(f"The winner is {winner} and the bid amount is ${max_cost}")

print(logo)
print("Welcome to the secret auction program.")

bid={}
next_user = True
while next_user == True:
    user_name = input("What is your name?: ")
    user_cost = int(input("What is your bid?: $"))
    question = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    bid[user_name] = user_cost
    if question == "no":
        next_user = False
        bidding(bid)
    elif question == "yes":
        os.system('clear')
        
