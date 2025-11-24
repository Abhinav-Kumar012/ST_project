import unittest
from src.utils import *


class TestMathUtilities(unittest.TestCase):
    def test_factorial_invalid(self):
        self.assertIsNone(factorial(3.5))
        self.assertIsNone(factorial(-1))

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)

    def test_fibonacci_invalid(self):
        self.assertIsNone(fibonacci(2.3))
        self.assertIsNone(fibonacci(-4))

    def test_fibonacci_base(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_normal(self):
        self.assertEqual(fibonacci(7), 13)

    def test_is_prime_invalid(self):
        self.assertFalse(is_prime(2.5))

    def test_is_prime_small(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))

    def test_is_prime_composites(self):
        self.assertFalse(is_prime(9))
        self.assertTrue(is_prime(29))

    def test_gcd_invalid(self):
        self.assertIsNone(gcd("a", 5))

    def test_gcd_valid(self):
        self.assertEqual(gcd(48, 18), 6)

    def test_lcm_invalid(self):
        self.assertIsNone(lcm("x", 10))

    def test_lcm_zero(self):
        self.assertEqual(lcm(0, 10), 0)

    def test_lcm_normal(self):
        self.assertEqual(lcm(4, 6), 12)

    def test_power_invalid(self):
        self.assertIsNone(power("a", 3))
        self.assertIsNone(power(2, 3.2))

    def test_power_zero_exp(self):
        self.assertEqual(power(5, 0), 1)

    def test_power_positive(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_negative(self):
        self.assertAlmostEqual(power(2, -3), 1 / 8)

    def test_solve_quadratic_invalid(self):
        self.assertIsNone(solve_quadratic(0, 2, 1))

    def test_solve_quadratic_no_real(self):
        self.assertEqual(solve_quadratic(1, 0, 1), [])

    def test_solve_quadratic_single(self):
        self.assertEqual(solve_quadratic(1, 2, 1), [-1])

    def test_solve_quadratic_two(self):
        roots = solve_quadratic(1, 0, -1)
        self.assertIn(1, roots)
        self.assertIn(-1, roots)


class TestStringUtilities(unittest.TestCase):
    def test_is_palindrome_invalid(self):
        self.assertFalse(is_palindrome(10))

    def test_is_palindrome_true(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome("hello"))

    def test_reverse_string_invalid(self):
        self.assertIsNone(reverse_string(5))

    def test_reverse_string_valid(self):
        self.assertEqual(reverse_string("abc"), "cba")

    def test_count_vowels_invalid(self):
        self.assertIsNone(count_vowels(3))

    def test_count_vowels_valid(self):
        self.assertEqual(count_vowels("Hello"), 2)

    def test_caesar_cipher_invalid(self):
        self.assertIsNone(caesar_cipher(123, 2))

    def test_caesar_cipher_valid(self):
        self.assertEqual(caesar_cipher("abc", 1), "bcd")
        self.assertEqual(caesar_cipher("XYZ", 2), "ZAB")


class TestListUtilities(unittest.TestCase):
    def test_bubble_sort_invalid(self):
        self.assertIsNone(bubble_sort("not_list"))

    def test_bubble_sort_valid(self):
        self.assertEqual(bubble_sort([3, 1, 2]), [1, 2, 3])

    def test_binary_search_invalid(self):
        self.assertEqual(binary_search("oops", 2), -1)

    def test_binary_search_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4], 3), 2)

    def test_binary_search_not_found(self):
        self.assertEqual(binary_search([1, 2, 3], 5), -1)

    def test_list_sum_invalid(self):
        self.assertIsNone(list_sum("nope"))

    def test_list_sum_valid(self):
        self.assertEqual(list_sum([1, "a", 2.5]), 3.5)

    def test_list_max_invalid(self):
        self.assertIsNone(list_max("no"))
        self.assertIsNone(list_max([]))

    def test_list_max_valid(self):
        self.assertEqual(list_max([1, 3, 2]), 3)

    def test_list_min_invalid(self):
        self.assertIsNone(list_min("bad"))
        self.assertIsNone(list_min([]))

    def test_list_min_valid(self):
        self.assertEqual(list_min([3, 1, 2]), 1)

    def test_remove_duplicates_invalid(self):
        self.assertIsNone(remove_duplicates("no"))

    def test_remove_duplicates_valid(self):
        self.assertEqual(remove_duplicates([1, 2, 1, 3]), [1, 2, 3])

    def test_merge_lists_invalid(self):
        self.assertIsNone(merge_lists("a", []))

    def test_merge_lists_valid(self):
        self.assertEqual(merge_lists([1, 3], [2, 4]), [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
