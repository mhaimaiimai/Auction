import os
is_endAuction = False
winner_bid = 0
auction_history = {}

while (not is_endAuction):
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    if not bid in auction_history:
        auction_history = {bid: name}
    else:
        auction_history[bid] += " and " + name
    
    if bid > winner_bid:
        winner_bid = bid

    if input("Are there any other bidders? Type 'yes' or 'no'.\n") == "yes":
        os.system('clear')
    else:
        is_endAuction = True
        print(f"The winner is {auction_history[bid]} with a bid of ${bid}")