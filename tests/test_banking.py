import unittest
from src.banking import Account, Bank

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.acc = Account(100)

    def test_deposit_success(self):
        result = self.acc.deposit(50)
        self.assertTrue(result)
        self.assertEqual(self.acc.get_balance(), 150)

    def test_deposit_failure(self):
        result = self.acc.deposit(-10)
        self.assertFalse(result)
        self.assertEqual(self.acc.get_balance(), 100)

    def test_withdraw_success(self):
        result = self.acc.withdraw(50)
        self.assertTrue(result)
        self.assertEqual(self.acc.get_balance(), 50)

    def test_withdraw_insufficient_funds(self):
        result = self.acc.withdraw(150)
        self.assertFalse(result)
        self.assertEqual(self.acc.get_balance(), 100)

    def test_withdraw_negative(self):
        result = self.acc.withdraw(-10)
        self.assertFalse(result)
        self.assertEqual(self.acc.get_balance(), 100)


class TestBankIntegration(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.acc1 = Account(100)
        self.acc2 = Account(50)
        self.bank.add_account("acc1", self.acc1)
        self.bank.add_account("acc2", self.acc2)

    def test_transfer_success(self):
        result = self.bank.transfer("acc1", "acc2", 50)
        self.assertTrue(result)
        self.assertEqual(self.acc1.get_balance(), 50)
        self.assertEqual(self.acc2.get_balance(), 100)

    def test_transfer_insufficient_funds(self):
        result = self.bank.transfer("acc1", "acc2", 150)
        self.assertFalse(result)
        self.assertEqual(self.acc1.get_balance(), 100)
        self.assertEqual(self.acc2.get_balance(), 50)

    def test_transfer_invalid_accounts(self):
        result = self.bank.transfer("acc1", "acc3", 50)
        self.assertFalse(result)
        self.assertEqual(self.acc1.get_balance(), 100)

if __name__ == '__main__':
    unittest.main()
