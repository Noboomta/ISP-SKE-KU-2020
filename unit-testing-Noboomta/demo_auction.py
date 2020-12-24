from auction import Auction
import random
#
# Demonstrate use of the Auction class.
#

def demo_auction():
    """Run a random auction.  Stop after max_bids bids."""
    # number of bids to accept
    max_bids = 10
    auction = Auction("Vacation to Ko Samui")
    auction.start()
    print("Starting", auction, "with min bidding increment", auction.increment)
    #auction.bid("initial", 20)
    for n in range(0,max_bids):
        bidder = get_bidder(auction)
        amount = int(auction.best_bid() + 10*random.randint(-2,5) + 10)
        print_and_bid(auction,bidder,amount)
        # pause the auction
        if n == max_bids/2:
            print(">>> stop()")
            auction.stop()
        elif n == max_bids/2 + 1:
            print(">>> start()")
            auction.start()
        
    print("The winner is", auction.winner(), "with a bid of", auction.best_bid())

def get_bidder(auction):
    """get a random bidder"""
    bidders = ["Ant", "Bat", "Cat", "Dog" ]
    winner = auction.winner()
    if winner in bidders:
        start = bidders.index(winner)
    else:
        start = -1
    # this avoids selecting the same bidder again
    nextbidder = (start + random.randint(1,len(bidders)-1)) % len(bidders)
    return bidders[nextbidder]
    
def print_and_bid(auction, bidder, amount):
    print(f'>>> bid( {bidder}, {amount} )')
    try:
        auction.bid(bidder, amount)
    except Exception as e:
        ex_name = type(e).__name__
        print(f'{ex_name}:', e)

if __name__ == "__main__":
    demo_auction()
