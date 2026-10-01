# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from operator import truediv

import art
print(art.logo)
print("Welcome to the secret auction program!")

bid_dictionary = {}

other_bidders_present = True

while other_bidders_present:

    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
    bid_dictionary[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if other_bidders == "no":
        other_bidders_present = False
        print("\n"*100)
    else:
        print("\n"*100)
        print(art.logo)
        print("Welcome to the secret auction program!")

def find_max_bidder(bid_dictionary):

    max_name = ""
    max_bid = 0


    for key in bid_dictionary:
        if bid_dictionary[key] > max_bid:
            max_bid = bid_dictionary[key]
            max_name = key

    print(f"The winner is {max_name} with a bid of ${max_bid}")

find_max_bidder(bid_dictionary)