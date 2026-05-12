logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("WELCOME TO THE SECRET AUCTION")
bids = {}
continue_auction = True
while continue_auction:
    name = input("What is your name? : ")
    price = int(input("What's your bid? : $"))
    bids[name] = price
    should_continue =  input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if should_continue == "yes":
        print("\n" * 100)
    elif should_continue == "no":
        continue_auction = False
highest_bid = 0
winner = ""
for bidder in bids:
    if bids[bidder] > max:
        highest_bid = bids[bidder]
        winner = bidder

print(f"The winner is {winner} with a bid of ${max}")