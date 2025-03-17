art = " '''''''" \
      "''''''''''" \
      "'''''''''" \
      "    ''   '''   '' '''    '' '''" \
      "  '' xxx oooooo"


def highest_bidder():
    highest_bid = int(0)
    bidder_name = ''
    for bidder in bidding_list:
        # print(bidder)
        if bidding_list[bidder] > highest_bid:
            print("TRUE")
            highest_bid = bidding_list[bidder]
            bidder_name = bidder
    print(f"Highest Bidder is: {bidder_name}")


print("Welcome to the art gallery! Here's your art:", art)

bidding_list = {}

while True:
    name = input("What is your name? ")
    bid_amount = input("How much do you bid? $")

    bidding_list[name] = int(bid_amount)
    print(bidding_list)

    bid_further = input("Do you want to continue? Type 'y' or 'n'").lower()

    if bid_further == 'n':
        print("Thank you!")
        break

print(f"Here's the bidding list: ", bidding_list)

highest_bidder()
