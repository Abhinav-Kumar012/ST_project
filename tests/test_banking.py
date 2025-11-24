import unittest
from src.banking import Account, Bank,Transaction, SavingsAccount, CheckingAccount
import time
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

###  ---- -----
class TestTransaction(unittest.TestCase):
    def test_transaction_creation(self):
        t = Transaction("DEPOSIT", 100)
        self.assertEqual(t.type, "DEPOSIT")
        self.assertEqual(t.amount, 100)
        self.assertTrue(isinstance(t.timestamp, float))
        repr_str = repr(t)
        self.assertIn("DEPOSIT", repr_str)
        self.assertIn("100", repr_str)


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.acc = Account(50)

    def test_initial_balance(self):
        self.assertEqual(self.acc.get_balance(), 50)

    def test_deposit_positive(self):
        self.assertTrue(self.acc.deposit(30))
        self.assertEqual(self.acc.get_balance(), 80)
        self.assertEqual(len(self.acc.get_transaction_history()), 1)
        self.assertEqual(self.acc.get_transaction_history()[-1].type, "DEPOSIT")

    def test_deposit_negative(self):
        self.assertFalse(self.acc.deposit(-10))
        self.assertEqual(self.acc.get_balance(), 50)  # unchanged

    def test_withdraw_success(self):
        self.assertTrue(self.acc.withdraw(20))
        self.assertEqual(self.acc.get_balance(), 30)
        self.assertEqual(self.acc.get_transaction_history()[-1].type, "WITHDRAWAL")

    def test_withdraw_fail_insufficient(self):
        self.assertFalse(self.acc.withdraw(100))
        self.assertEqual(self.acc.get_balance(), 50)

    def test_withdraw_negative(self):
        self.assertFalse(self.acc.withdraw(-5))
        self.assertEqual(self.acc.get_balance(), 50)

    def test_transaction_history(self):
        self.acc.deposit(10)
        self.acc.withdraw(5)
        history = self.acc.get_transaction_history()
        self.assertEqual(len(history), 2)
        self.assertEqual(history[0].type, "DEPOSIT")
        self.assertEqual(history[1].type, "WITHDRAWAL")


class TestSavingsAccount(unittest.TestCase):
    def test_interest_application(self):
        sa = SavingsAccount(100, 0.05)
        time.sleep(0.01)  # ensure timestamp changes for coverage
        sa.apply_interest()
        self.assertAlmostEqual(sa.get_balance(), 105)
        self.assertEqual(sa.get_transaction_history()[-1].type, "INTEREST")


class TestCheckingAccount(unittest.TestCase):
    def test_overdraft_allowed(self):
        ca = CheckingAccount(initial_balance=50, overdraft_limit=30)
        self.assertTrue(ca.withdraw(70))
        self.assertEqual(ca.get_balance(), -20)

    def test_overdraft_denied(self):
        ca = CheckingAccount(initial_balance=50, overdraft_limit=30)
        self.assertFalse(ca.withdraw(90))  # beyond limit
        self.assertEqual(ca.get_balance(), 50)

    def test_normal_withdrawal(self):
        ca = CheckingAccount(100)
        self.assertTrue(ca.withdraw(20))
        self.assertEqual(ca.get_balance(), 80)


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.bank.add_account("A", Account(100))
        self.bank.add_account("B", Account(50))

    def test_add_and_get_account(self):
        acc = self.bank.get_account("A")
        self.assertIsNotNone(acc)
        self.assertEqual(acc.get_balance(), 100)

    def test_transfer_success(self):
        result = self.bank.transfer("A", "B", 40)
        self.assertTrue(result)
        self.assertEqual(self.bank.get_account("A").get_balance(), 60)
        self.assertEqual(self.bank.get_account("B").get_balance(), 90)
        self.assertEqual(self.bank.get_account("A").transactions[-1].type, "TRANSFER_OUT_TO_B")
        self.assertEqual(self.bank.get_account("B").transactions[-1].type, "TRANSFER_IN_FROM_A")

    def test_transfer_invalid_ids(self):
        self.assertFalse(self.bank.transfer("A", "X", 10))
        self.assertFalse(self.bank.transfer("X", "A", 10))

    def test_transfer_insufficient_funds(self):
        result = self.bank.transfer("A", "B", 1000)
        self.assertFalse(result)
        self.assertEqual(self.bank.get_account("A").get_balance(), 100)
        self.assertEqual(self.bank.get_account("B").get_balance(), 50)

    def test_transfer_deposit_fail_rollback(self):
        # Create failing deposit scenario
        class FailDepositAccount(Account):
            def deposit(self, amount):
                return False

        self.bank.add_account("C", FailDepositAccount(0))

        result = self.bank.transfer("A", "C", 20)
        self.assertFalse(result)

        # Check rollback happened (balance unchanged)
        self.assertEqual(self.bank.get_account("A").get_balance(), 100)

    def test_total_deposits(self):
        total = self.bank.get_total_deposits()
        self.assertEqual(total, 150)


if __name__ == "__main__":
    unittest.main()
