import math
import unittest

from src.stats_lib import *


class TestStatistics(unittest.TestCase):
    def test_mean_normal(self):
        self.assertEqual(mean([1, 2, 3]), 2)

    def test_mean_empty(self):
        self.assertIsNone(mean([]))

    def test_median_odd(self):
        self.assertEqual(median([3, 1, 2]), 2)

    def test_median_even(self):
        self.assertEqual(median([4, 2, 1, 3]), 2.5)

    def test_median_empty(self):
        self.assertIsNone(median([]))

    def test_mode_single(self):
        self.assertEqual(mode([1, 1, 2]), 1)

    def test_mode_multiple(self):
        result = mode([1, 1, 2, 2])
        self.assertEqual(set(result), {1, 2})

    def test_mode_empty(self):
        self.assertIsNone(mode([]))

    def test_variance_population(self):
        self.assertAlmostEqual(variance([1, 2, 3], True), 2 / 3)

    def test_variance_sample(self):
        self.assertAlmostEqual(variance([1, 2, 3], False), 1)

    def test_variance_invalid(self):
        self.assertIsNone(variance([], True))
        self.assertIsNone(variance([1], True))

    def test_std_dev_population(self):
        self.assertAlmostEqual(std_dev([1, 2, 3], True), math.sqrt(2 / 3))

    def test_std_dev_invalid(self):
        self.assertIsNone(std_dev([], True))

    def test_covariance_population(self):
        self.assertAlmostEqual(covariance([1, 2, 3], [1, 2, 3]), 2 / 3)

    def test_covariance_sample(self):
        self.assertAlmostEqual(covariance([1, 2, 3], [1, 2, 3], False), 1)

    def test_covariance_invalid(self):
        self.assertIsNone(covariance([1], [1]))
        self.assertIsNone(covariance([1, 2], [1]))

    def test_correlation_normal(self):
        self.assertEqual(correlation([1, 2, 3], [1, 2, 3]), 1)

    def test_correlation_zero_variance(self):
        self.assertIsNone(correlation([1, 1, 1], [1, 2, 3]))

    def test_correlation_invalid(self):
        self.assertIsNone(correlation([1], [1]))

    def test_linear_regression_normal(self):
        slope, intercept = linear_regression([1, 2, 3], [2, 4, 6])
        self.assertEqual(slope, 2)
        self.assertEqual(intercept, 0)

    def test_linear_regression_invalid_lengths(self):
        self.assertIsNone(linear_regression([1, 2], [3]))

    def test_linear_regression_zero_denominator(self):
        self.assertIsNone(linear_regression([5, 5, 5], [1, 2, 3]))

    def test_zscore_normal(self):
        self.assertAlmostEqual(z_score([1, 2, 3], 2), 0.0)

    def test_zscore_invalid(self):
        self.assertIsNone(z_score([1, 1, 1], 1))
        self.assertIsNone(z_score([], 5))

    def test_percentile_exact(self):
        self.assertEqual(percentile([10, 20, 30], 50), 20)

    def test_percentile_interpolated(self):
        self.assertEqual(percentile([10, 20, 30], 25), 15)

    def test_percentile_invalid(self):
        self.assertIsNone(percentile([], 50))
        self.assertIsNone(percentile([1, 2, 3], -10))
        self.assertIsNone(percentile([1, 2, 3], 110))

    def test_iqr_normal(self):
        expected = percentile([1, 2, 3, 4], 75) - percentile([1, 2, 3, 4], 25)
        self.assertEqual(iqr([1, 2, 3, 4]), expected)

    def test_iqr_invalid(self):
        self.assertIsNone(iqr([]))

    def test_skewness_normal(self):
        val = skewness([1, 2, 3])
        self.assertTrue(isinstance(val, float))

    def test_skewness_invalid(self):
        self.assertIsNone(skewness([]))
        self.assertIsNone(skewness([1, 1, 1]))

    def test_kurtosis_normal(self):
        val = kurtosis([1, 2, 3, 4])
        self.assertTrue(isinstance(val, float))

    def test_kurtosis_invalid(self):
        self.assertIsNone(kurtosis([]))
        self.assertIsNone(kurtosis([1, 1, 1, 1]))


if __name__ == "__main__":
    unittest.main()
