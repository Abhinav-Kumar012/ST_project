import unittest
from src import utils

class TestUtils(unittest.TestCase):
    def test_math_utils(self):
        self.assertEqual(utils.factorial(5), 120)
        self.assertEqual(utils.fibonacci(10), 55)
        self.assertTrue(utils.is_prime(17))
        self.assertEqual(utils.gcd(48, 18), 6)
        self.assertEqual(utils.lcm(4, 6), 12)
        self.assertEqual(utils.power(2, 3), 8)
        self.assertEqual(utils.solve_quadratic(1, -3, 2), [2.0, 1.0])

    def test_string_utils(self):
        self.assertTrue(utils.is_palindrome("racecar"))
        self.assertEqual(utils.reverse_string("hello"), "olleh")
        self.assertEqual(utils.count_vowels("hello"), 2)
        self.assertEqual(utils.caesar_cipher("abc", 1), "bcd")

    def test_list_utils(self):
        self.assertEqual(utils.bubble_sort([3, 1, 2]), [1, 2, 3])
        self.assertEqual(utils.binary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(utils.list_sum([1, 2, 3]), 6)
        self.assertEqual(utils.list_max([1, 5, 2]), 5)
        self.assertEqual(utils.list_min([1, 5, 2]), 1)
        self.assertEqual(utils.remove_duplicates([1, 2, 2, 3]), [1, 2, 3])
        self.assertEqual(utils.merge_lists([1, 3], [2, 4]), [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
