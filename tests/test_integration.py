import unittest
import math
from src import utils, geometry, banking, stats_lib

class TestIntegrationScenarios(unittest.TestCase):
    def test_complex_financial_geometry_scenario(self):
        # 1. Math: Solve quadratic equation x^2 - 10x + 21 = 0
        # Roots should be (10 +/- sqrt(100 - 84))/2 = (10 +/- 4)/2 -> 7 and 3
        roots = utils.solve_quadratic(1, -10, 21)
        self.assertIsNotNone(roots)
        self.assertEqual(sorted(roots), [3.0, 7.0])
        
        width = min(roots)
        height = max(roots)

        # 2. Geometry: Create Rectangle from roots
        rect = geometry.Rectangle(geometry.Point2D(0, height), width, height)
        area = rect.area()
        self.assertEqual(area, 21.0)

        # 3. Banking: Open SavingsAccount with area as initial balance
        # Interest rate 10% for easy calculation
        account = banking.SavingsAccount(initial_balance=area, interest_rate=0.10)
        self.assertEqual(account.get_balance(), 21.0)

        # 4. Banking: Apply interest
        # 21 + 10% = 21 + 2.1 = 23.1
        account.apply_interest()
        self.assertAlmostEqual(account.get_balance(), 23.1)

        # 5. Banking: Withdraw the smaller root (3.0)
        # 23.1 - 3.0 = 20.1
        success = account.withdraw(width)
        self.assertTrue(success)
        self.assertAlmostEqual(account.get_balance(), 20.1)

        # 6. Statistics: Analyze transaction history
        # History: 
        # - DEPOSIT 21.0 (Initial) -> Wait, initial balance might not be a transaction in __init__?
        # Let's check banking.py... __init__ sets self.balance but doesn't append to transactions.
        # So transactions are:
        # 1. INTEREST (Deposit 2.1)
        # 2. WITHDRAWAL (3.0)
        
        history = account.get_transaction_history()
        self.assertEqual(len(history), 2)
        
        amounts = [t.amount for t in history]
        # [2.1, 3.0]
        
        mean_amount = stats_lib.mean(amounts)
        # (2.1 + 3.0) / 2 = 5.1 / 2 = 2.55
        self.assertAlmostEqual(mean_amount, 2.55)
        
        std_dev = stats_lib.std_dev(amounts, population=True)
        # Variance = ((2.1-2.55)^2 + (3.0-2.55)^2) / 2
        # = ((-0.45)^2 + (0.45)^2) / 2
        # = (0.2025 + 0.2025) / 2 = 0.2025
        # StdDev = sqrt(0.2025) = 0.45
        self.assertAlmostEqual(std_dev, 0.45)

if __name__ == '__main__':
    unittest.main()
