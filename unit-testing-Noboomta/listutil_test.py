import unittest
from listutil import unique

class ListUtilTest(unittest.TestCase):
    """
    Unit test class to test the unique function.
    """    

    def test_single_item_list(self):
        self.assertListEqual( ['hi'], unique(['hi']) )

    def test_empty_list(self):
        self.assertListEqual( [], unique([]))
    
    def test_argument_not_a_list(self):
        self.assertRaises(TypeError, unique("abc"))
 
if __name__ == '__main__':
    unittest.main()