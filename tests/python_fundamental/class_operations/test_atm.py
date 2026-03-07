import unittest
from src.python_fundamental.class_operations.atm import ATM


class TestATM(unittest.TestCase):

    # setUp() create a new ATM object before each test
    def setUp(self):
        self.atm = ATM()

    # test initial balance
    def test_initial_balance(self):
        self.assertEqual(self.atm.get_balance(), 0)

    # test deposit operation
    def test_deposit(self):
        result = self.atm.deposit(100)

        # check return message
        self.assertEqual(result, "100 deposited successfully")

        # check updated balance
        self.assertEqual(self.atm.get_balance(), 100)

    # test withdraw when balance is sufficient
    def test_withdraw_success(self):
        self.atm.deposit(200)

        result = self.atm.withdraw(50)

        self.assertEqual(result, "50 withdrawn successfully")
        self.assertEqual(self.atm.get_balance(), 150)

    # test withdraw when balance is insufficient
    def test_withdraw_insufficient_balance(self):
        result = self.atm.withdraw(100)

        self.assertEqual(result, "Insufficient balance")
        self.assertEqual(self.atm.get_balance(), 0)

    # edge case: withdraw full balance
    def test_withdraw_full_balance(self):
        self.atm.deposit(100)

        self.atm.withdraw(100)

        self.assertEqual(self.atm.get_balance(), 0)


if __name__ == "__main__":
    unittest.main()
