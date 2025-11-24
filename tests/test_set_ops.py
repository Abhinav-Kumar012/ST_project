import unittest
from src.set_ops import (
    set_union,
    set_intersection,
    set_difference,
    set_symmetric_difference,
    is_subset,
    power_set,
    cartesian_product,
    jaccard_similarity
)

class TestSetOperations(unittest.TestCase):

    def test_set_union_normal(self):
        self.assertEqual(set_union([1,2], [2,3]), [1,2,3])

    def test_set_union_duplicates(self):
        self.assertEqual(set_union([1,1,2], [2,2,3]), [1,2,3])

    def test_set_union_non_list(self):
        self.assertIsNone(set_union(5, [1,2]))

    def test_set_intersection_normal(self):
        self.assertEqual(set_intersection([1,2,3], [2,3,4]), [2,3])

    def test_set_intersection_no_overlap(self):
        self.assertEqual(set_intersection([1,2], [3,4]), [])

    def test_set_intersection_non_list(self):
        self.assertIsNone(set_intersection("abc", [1,2]))

    def test_set_difference_normal(self):
        self.assertEqual(set_difference([1,2,3], [2]), [1,3])

    def test_set_difference_no_difference(self):
        self.assertEqual(set_difference([1], [1]), [])

    def test_set_difference_non_list(self):
        self.assertIsNone(set_difference([1,2], None))

    def test_symmetric_difference_normal(self):
        self.assertEqual(set_symmetric_difference([1,2], [2,3]), [1,3])

    def test_symmetric_difference_identical(self):
        self.assertEqual(set_symmetric_difference([1,2], [1,2]), [])

    def test_symmetric_difference_non_list(self):
        self.assertIsNone(set_symmetric_difference(1, [1]))

    def test_is_subset_true(self):
        self.assertTrue(is_subset([1,2], [1,2,3]))

    def test_is_subset_false(self):
        self.assertFalse(is_subset([1,4], [1,2,3]))

    def test_is_subset_non_list(self):
        self.assertFalse(is_subset(1, [1,2]))

    def test_power_set_normal(self):
        self.assertEqual(power_set([1,2]), [[], [1], [2], [1,2]])

    def test_power_set_empty(self):
        self.assertEqual(power_set([]), [[]])

    def test_power_set_non_list(self):
        self.assertIsNone(power_set("abc"))

    def test_cartesian_product_normal(self):
        self.assertEqual(
            cartesian_product([1,2], ['a']),
            [(1,'a'), (2,'a')]
        )

    def test_cartesian_product_empty(self):
        self.assertEqual(cartesian_product([], [1]), [])

    def test_cartesian_product_non_list(self):
        self.assertIsNone(cartesian_product([1,2], None))

    def test_jaccard_similarity_normal(self):
        self.assertAlmostEqual(jaccard_similarity([1,2], [2,3]), 1/3)

    def test_jaccard_similarity_both_empty(self):
        self.assertEqual(jaccard_similarity([], []), 0.0)

    def test_jaccard_similarity_union_empty_but_intersection_exists(self):
        self.assertEqual(jaccard_similarity(None, None), 0.0)

    def test_jaccard_similarity_full_overlap(self):
        self.assertEqual(jaccard_similarity([1,2], [1,2]), 1.0)

    def test_jaccard_similarity_no_intersection(self):
        self.assertEqual(jaccard_similarity([1], [2]), 0.0)


if __name__ == "__main__":
    unittest.main()
