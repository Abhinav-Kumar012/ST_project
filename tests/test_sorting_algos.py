import unittest
from src.sorting_algos import *


class TestSortingAlgorithms(unittest.TestCase):
    def test_quick_sort_empty(self):
        self.assertEqual(quick_sort([]), [])

    def test_quick_sort_single(self):
        self.assertEqual(quick_sort([5]), [5])

    def test_quick_sort_general(self):
        self.assertEqual(quick_sort([3, 1, 2, 5, 4]), [1, 2, 3, 4, 5])

    def test_quick_sort_duplicates(self):
        self.assertEqual(quick_sort([3, 3, 3]), [3, 3, 3])

    def test_quick_sort_reverse(self):
        self.assertEqual(quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_merge_sort_empty(self):
        self.assertEqual(merge_sort([]), [])

    def test_merge_sort_single(self):
        self.assertEqual(merge_sort([10]), [10])

    def test_merge_sort_general(self):
        self.assertEqual(merge_sort([4, 2, 1, 3]), [1, 2, 3, 4])

    def test_heap_sort_empty(self):
        self.assertEqual(heap_sort([]), [])

    def test_heap_sort_single(self):
        self.assertEqual(heap_sort([8]), [8])

    def test_heap_sort_general(self):
        arr = [4, 10, 3, 5, 1]
        self.assertEqual(heap_sort(arr), [1, 3, 4, 5, 10])

    def test_shell_sort_empty(self):
        self.assertEqual(shell_sort([]), [])

    def test_shell_sort_single(self):
        self.assertEqual(shell_sort([8]), [8])

    def test_shell_sort_general(self):
        self.assertEqual(shell_sort([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])

    def test_selection_sort_empty(self):
        self.assertEqual(selection_sort([]), [])

    def test_selection_sort_single(self):
        self.assertEqual(selection_sort([9]), [9])

    def test_selection_sort_general(self):
        self.assertEqual(selection_sort([4, 2, 5, 1]), [1, 2, 4, 5])

    def test_insertion_sort_empty(self):
        self.assertEqual(insertion_sort([]), [])

    def test_insertion_sort_single(self):
        self.assertEqual(insertion_sort([6]), [6])

    def test_insertion_sort_general(self):
        self.assertEqual(insertion_sort([3, 1, 2]), [1, 2, 3])

    def test_insertion_sort_reverse(self):
        self.assertEqual(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
