from unittest.result import failfast
from check import Check
from money import Money
import unittest
from bank_account import BankAccount
from unittest import TestCase

def set_up():
    """ method to set the bank_account"""
    bank_account = BankAccount("Boom", 1000)
    return bank_account

class BankAccountTest(unittest.TestCase):

    def test_name(self):
        """ test if name is equal with the generation process. """
        bank_account = set_up()
        self.assertEqual(bank_account.account_name, "Boom")

    def test_balance(self):
        """ test if balance is correct. """
        bank_account = set_up()
        bank_account.deposit( Money(9000) )
        self.assertEqual(bank_account.balance, 9000)

    def test_available(self):
        """ test if available is correct. """
        bank_account = set_up()
        bank_account.deposit( Money(9000) )
        self.assertEqual(bank_account.available, 8000)

    def test_negative_withdraw(self):
        """ test that raise the ValueError after withdraw the negative value. """
        bank_account = set_up()
        bank_account.deposit( Money(9000) )
        with self.assertRaises(ValueError):
            bank_account.withdraw(-10000)

    def test_too_much_withdraw(self):
        """ test that raise the ValueError after withdraw higher than available. """
        bank_account = set_up()
        bank_account.deposit( Money(9000) )
        ck = Check(10000)
        bank_account.deposit(ck)
        with self.assertRaises(ValueError):
            bank_account.withdraw(10000)

    def test_balance_and_availablechanged_after_withdraw(self):
        """ test if the balance and available is correct after withdraw. """
        bank_account = set_up()
        bank_account.deposit( Money(9000) )
        wd = bank_account.withdraw(2500)
        self.assertEqual(wd, Money(2500))
        self.assertEqual(bank_account.balance, 6500)
        self.assertEqual(bank_account.available, 5500)

    def test_balance_changed_after_check_added(self):
        """ test if the balance is changed after deposit check. """
        bank_account = set_up()
        ck = Check(5000)
        bank_account.deposit(ck)
        self.assertEqual(bank_account.balance, 5000)

    def test_balance_changed_after_check_added(self):
        """ test if the balance and available is changed after deposit and clear check. """
        bank_account = set_up()
        ck = Check(5000)
        self.assertEqual(ck.check_number, Check._next_check_number-1)
        bank_account.deposit(ck)
        self.assertEqual(bank_account.available, 0)
        bank_account.clear_check(ck)
        self.assertEqual(bank_account.available, 4000)

    def test_negative_deposit(self):
        """ test if the min_balance is correct. """
        bank_account = set_up()
        with self.assertRaises(ValueError):
            bank_account.deposit(Money(-1000))
        with self.assertRaises(ValueError):
            bank_account.deposit(Check(-1000))

    def test_check_in_peding_check(self):
        """ test if the ValueError raised after deposit a deposited check. """
        bank_account = set_up()
        ck = Check(1000)
        with self.assertRaises(ValueError):
            bank_account.deposit(ck)
            bank_account.deposit(ck)
    
    def test_can_add_the_check_again_after_clear_check(self):
        """ test if the  """
        bank_account = set_up()
        ck = Check(1000)
        bank_account.deposit(ck)
        bank_account.clear_check(ck)
        self.assertEqual(bank_account.balance, 1000)
        bank_account.deposit(ck)
        bank_account.clear_check(ck)
        self.assertEqual(bank_account.balance, 2000)
            
    def test_ValueError_raised_after_clear_check_with_not_deposited(self):
        """ test if the ValueError raised after clear_check with the check 
        which not in the pending check. """
        bank_account = set_up()
        ck1 = Check(7890)
        fake_check = Check(1234)
        bank_account.deposit(ck1)
        with self.assertRaises(ValueError):
            bank_account.clear_check(fake_check)

if __name__ == "__main__":
    unittest.main()