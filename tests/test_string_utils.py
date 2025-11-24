import unittest

from src.string_utils import (
    is_palindrome,
    is_anagram,
    levenshtein_distance,
    to_camel_case,
    to_snake_case,
    count_vowels,
    reverse_words,
    longest_common_substring
)


class TestStringUtils(unittest.TestCase):
    def test_palindrome_normal(self):
        self.assertTrue(is_palindrome("Racecar"))

    def test_palindrome_with_non_alnum(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama!"))

    def test_palindrome_false(self):
        self.assertFalse(is_palindrome("hello"))

    def test_palindrome_invalid_type(self):
        self.assertFalse(is_palindrome(123))

    def test_anagram_normal(self):
        self.assertTrue(is_anagram("Listen", "Silent"))

    def test_anagram_false(self):
        self.assertFalse(is_anagram("hello", "world"))

    def test_anagram_non_alnum(self):
        self.assertTrue(is_anagram("Dormitory!!", "Dirty room"))

    def test_anagram_invalid_type(self):
        self.assertFalse(is_anagram("abc", 123))

    def test_levenshtein_normal(self):
        self.assertEqual(levenshtein_distance("kitten", "sitting"), 3)

    def test_levenshtein_swap_len_branch(self):
        self.assertEqual(levenshtein_distance("a", "abc"), 2)

    def test_levenshtein_empty_s2(self):
        self.assertEqual(levenshtein_distance("hello", ""), 5)

    def test_levenshtein_invalid(self):
        self.assertIsNone(levenshtein_distance("abc", 123))

    def test_camel_case_normal(self):
        self.assertEqual(to_camel_case("hello_world_test"), "helloWorldTest")

    def test_camel_case_single_word(self):
        self.assertEqual(to_camel_case("hello"), "hello")

    def test_camel_case_invalid(self):
        self.assertIsNone(to_camel_case(123))

    def test_snake_case_normal(self):
        self.assertEqual(to_snake_case("CamelCaseTest"), "camel_case_test")

    def test_snake_case_single(self):
        self.assertEqual(to_snake_case("Hello"), "hello")

    def test_snake_case_invalid(self):
        self.assertIsNone(to_snake_case(123))

    def test_count_vowels_normal(self):
        self.assertEqual(count_vowels("Hello"), 2)

    def test_count_vowels_upper(self):
        self.assertEqual(count_vowels("AEIOU"), 5)

    def test_count_vowels_invalid(self):
        self.assertEqual(count_vowels(123), 0)

    def test_reverse_words_normal(self):
        self.assertEqual(reverse_words("Hello world here"), "here world Hello")

    def test_reverse_words_single(self):
        self.assertEqual(reverse_words("Hello"), "Hello")

    def test_reverse_words_invalid(self):
        self.assertIsNone(reverse_words(123))

    def test_lcs_normal(self):
        self.assertEqual(longest_common_substring("abcdef", "zabcy"), "abc")

    def test_lcs_no_common(self):
        self.assertEqual(longest_common_substring("abc", "xyz"), "")

    def test_lcs_one_empty(self):
        self.assertEqual(longest_common_substring("", "abc"), "")
        self.assertEqual(longest_common_substring("abc", ""), "")


if __name__ == "__main__":
    unittest.main()
