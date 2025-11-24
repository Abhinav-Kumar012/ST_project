import unittest
from src.search_algos import *


class TestSearchAlgorithms(unittest.TestCase):
    def test_linear_search_found(self):
        self.assertEqual(linear_search([1, 2, 3, 4], 3), 2)

    def test_linear_search_not_found(self):
        self.assertEqual(linear_search([1, 2, 3], 10), -1)

    def test_linear_search_empty(self):
        self.assertEqual(linear_search([], 5), -1)

    def test_binary_search_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 4), 3)

    def test_binary_search_not_found(self):
        self.assertEqual(binary_search([1, 2, 4, 5], 3), -1)

    def test_binary_search_single_element_found(self):
        self.assertEqual(binary_search([10], 10), 0)

    def test_binary_search_single_element_not_found(self):
        self.assertEqual(binary_search([10], 5), -1)

    def test_binary_search_recursive_found(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search_recursive(arr, 5, 0, len(arr) - 1), 4)

    def test_binary_search_recursive_not_found(self):
        arr = [1, 3, 5, 7]
        self.assertEqual(binary_search_recursive(arr, 2, 0, len(arr) - 1), -1)

    def test_binary_search_recursive_empty(self):
        self.assertEqual(binary_search_recursive([], 1, 0, -1), -1)

    def test_jump_search_found(self):
        arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(jump_search(arr, 7), 7)

    def test_jump_search_not_found(self):
        arr = [0, 2, 4, 6, 8]
        self.assertEqual(jump_search(arr, 3), -1)

    def test_jump_search_first_element(self):
        arr = [3, 5, 7, 9]
        self.assertEqual(jump_search(arr, 3), 0)

    def test_exponential_search_empty(self):
        self.assertEqual(exponential_search([], 5), -1)

    def test_exponential_search_first_element(self):
        arr = [5, 10, 20]
        self.assertEqual(exponential_search(arr, 5), 0)

    def test_exponential_search_middle(self):
        arr = [2, 4, 6, 8, 10, 12]
        self.assertEqual(exponential_search(arr, 10), 4)

    def test_exponential_search_not_found(self):
        arr = [1, 3, 5, 7]
        self.assertEqual(exponential_search(arr, 6), -1)

    def test_interpolation_search_found(self):
        arr = [10, 20, 30, 40, 50]
        self.assertEqual(interpolation_search(arr, 40), 3)

    def test_interpolation_search_not_found(self):
        arr = [10, 20, 30, 40]
        self.assertEqual(interpolation_search(arr, 25), -1)

    def test_interpolation_search_single_found(self):
        arr = [100]
        self.assertEqual(interpolation_search(arr, 100), 0)

    def test_interpolation_search_single_not_found(self):
        arr = [100]
        self.assertEqual(interpolation_search(arr, 50), -1)

    def test_interpolation_search_low_high_exit(self):
        arr = [10, 10, 10]
        self.assertEqual(interpolation_search(arr, 20), -1)


if __name__ == "__main__":
    unittest.main()
