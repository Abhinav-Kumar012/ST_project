import unittest
import math
from src import integration

class TestIntegrationScenarios(unittest.TestCase):
    def test_complex_financial_geometry_scenario(self):
        mean_amount, std_dev = integration.test_complex_financial_geometry_scenario(1, -10, 21,0.1)


        self.assertAlmostEqual(mean_amount, 2.55)
        self.assertAlmostEqual(std_dev, 0.45)

if __name__ == '__main__':
    unittest.main()