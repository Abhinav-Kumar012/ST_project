import unittest
import math
from src import integration

class TestIntegrationScenarios(unittest.TestCase):
    def test_complex_financial_geometry_scenario(self):
        mean_amount, std_dev = integration.test_complex_financial_geometry_scenario(1, -10, 21,0.1)
        self.assertAlmostEqual(mean_amount, 4.55)
        self.assertAlmostEqual(std_dev, 2.45)
    def test_v2(self):
        t = integration.test_complex_financial_geometry_scenario(1, 5, 6,0.1)
        self.assertIsNone(t)
    def test_v3(self):
        mean_amount, std_dev= integration.test_complex_financial_geometry_scenario(1, -3, 0,0.1)
        self.assertIsNone(mean_amount)
        self.assertIsNone(std_dev)
    def test_v4(self):
        mean_amount, std_dev= integration.test_complex_financial_geometry_scenario(1, 3, 0,0.1)
        self.assertIsNone(mean_amount)
        self.assertIsNone(std_dev)




if __name__ == '__main__':
    unittest.main()