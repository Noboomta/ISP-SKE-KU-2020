import unittest
from auction import Auction, AuctionError

def setup():
    auction = Auction("Auction Test")
    auction.start()
    return auction

class AuctionTest(unittest.TestCase):

    def test_winner(self):
        """test if the winner is the highest bidder."""
        auction = setup()
        auction.bid("Boom Puvana", 100)
        auction.bid("Park Dyoungmoon", 200)
        self.assertEqual("Park Dyoungmoon", auction.winner())
        auction.bid("Dionys", 1000)
        self.assertEqual("Dionys", auction.winner())

    def test_best_bid(self):
        """test if the best_bid is the highest bid."""
        auction = setup()
        auction.bid("Boom Puvana", 100)
        auction.bid("Park Dyoungmoon", 200)
        self.assertEqual(200, auction.best_bid())
        auction.bid("Dionys", 1000)
        self.assertEqual(1000, auction.best_bid())

    def test_value_error_raises(self):
        """test if the ValueError raises after add no name of bidder, or value of bid is 0."""
        auction = setup()
        with self.assertRaises(ValueError):
            auction.bid("", 100)
            auction.bid("Boom Puvana", 0)

    def test_auction_error_raises_from_wrong_value_type(self):
        """test if the AuctionError raises after bid is too low different with the recent."""
        auction = setup()
        auction.bid("Boom Puvana", 100)
        with self.assertRaises(AuctionError):
            auction.bid("Park Dyoungmoon", 100.01)
            auction.bid("Dionys", 100.1)    

    def test_type_error_raises(self):
        """test if the TypeError raises after bidder name is not a string, or the bid value is not a number."""
        auction = setup()
        with self.assertRaises(TypeError):
            auction.bid(300, 100)
            auction.bid("Boom Puvana", "hundred")

    def test_auction_error_raises_after_auction_stopped(self):
        """test if the AuctionError raises after the not acceptable bid, or after the auction is stopped."""
        auction = setup()
        auction.stop()
        with self.assertRaises(AuctionError):
            auction.bid("Boom Puvana", 100)
            auction.bid("Park Dyoungmoon", 200)

    def test_auction_is_active(self):
        """test if the is_active method is false after the auction is stopped."""
        auction = setup()
        auction.bid("Boom Puvana", 100)
        self.assertTrue(auction.is_active())
        auction.stop()
        self.assertFalse(auction.is_active())

    def test_bidder_name_has_changed(self):
        """test if the format of the bidder name is changed from the unusable spacing."""
        auction = setup()
        auction.bid("    Boom Puvana", 100)
        self.assertEqual("Boom Puvana", auction.winner())
        auction.bid("dionys", 200)
        self.assertEqual("Dionys", auction.winner())

if __name__ == '__main__':
    unittest.main()