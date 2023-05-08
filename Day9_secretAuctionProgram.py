print("Welcome to the secret auction program.")

auction_program = {}
other_bidders = "yes"
while other_bidders == "yes":
  name = input("What is your name?: ")
  bid = input("What's your bid?: $")
  auction_program[name] = int(bid)
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

bidder = "" 
highest_bid = 0
for key in auction_program:
    if auction_program[key] > highest_bid:
        highest_bid = auction_program[key]
        bidder = key    
print(f"The winner is {bidder} with the bid of ${highest_bid}")