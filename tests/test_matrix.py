import unittest
from src.matrix_ops import *
class TestMatrixOperations(unittest.TestCase):

    def test_matrix_add_valid(self):
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        self.assertEqual(matrix_add(A, B), [[6, 8], [10, 12]])

    def test_matrix_add_invalid_types(self):
        self.assertIsNone(matrix_add(5, [1]))

    def test_matrix_add_dimension_mismatch(self):
        self.assertIsNone(matrix_add([[1, 2]], [[1, 2], [3, 4]]))

    def test_matrix_sub_valid(self):
        
        A = [[5, 5], [5, 5]]
        B = [[1, 2], [3, 4]]
        self.assertEqual(matrix_sub(A, B), [[4, 3], [2, 1]])

    def test_matrix_sub_invalid_types(self):
        self.assertIsNone(matrix_sub("x", [1]))

    def test_matrix_sub_dimension_mismatch(self):
        self.assertIsNone(matrix_sub([[1]], [[1, 2]]))

    def test_matrix_mul_valid(self):
        A = [[1, 2]]
        B = [[3], [4]]
        self.assertEqual(matrix_mul(A, B), [[11]])

    def test_matrix_mul_invalid_types(self):
        self.assertIsNone(matrix_mul("x", [[1]]))

    def test_matrix_mul_dimension_mismatch(self):
        self.assertIsNone(matrix_mul([[1, 2]], [[1, 2]]))

    def test_matrix_transpose_valid(self):
        A = [[1, 2, 3]]
        self.assertEqual(matrix_transpose(A), [[1], [2], [3]])

    def test_matrix_transpose_invalid(self):
        self.assertIsNone(matrix_transpose("x"))

    def test_matrix_determinant_invalid_type(self):
        self.assertIsNone(matrix_determinant("x"))

    def test_matrix_determinant_not_square(self):
        self.assertIsNone(matrix_determinant([[1, 2, 3]]))

    def test_matrix_determinant_1x1(self):
        self.assertEqual(matrix_determinant([[7]]), 7)

    def test_matrix_determinant_2x2(self):
        A = [[1, 2], [3, 4]]
        self.assertEqual(matrix_determinant(A), -2)

    def test_matrix_determinant_3x3(self):
        A = [
            [6, 1, 1],
            [4, -2, 5],
            [2, 8, 7]
        ]
        self.assertEqual(matrix_determinant(A), -306)

    def test_matrix_minor(self):
        A = [[1, 2], [3, 4]]
        self.assertEqual(matrix_minor(A, 0, 0), 4)

    def test_matrix_cofactor(self):
        A = [[1, 2], [3, 4]]
        self.assertEqual(matrix_cofactor(A), [[4, -3], [-2, 1]])

    def test_matrix_inverse_valid(self):
        A = [[4, 7], [2, 6]]
        inv = matrix_inverse(A)
        self.assertAlmostEqual(inv[0][0], 0.6)
        self.assertAlmostEqual(inv[0][1], -0.7)
        self.assertAlmostEqual(inv[1][0], -0.2)
        self.assertAlmostEqual(inv[1][1], 0.4)

    def test_matrix_inverse_singular(self):
        A = [[1, 2], [2, 4]]
        self.assertIsNone(matrix_inverse(A))

    def test_matrix_power_zero(self):
        A = [[2, 3], [4, 5]]
        self.assertEqual(matrix_power(A, 0), identity_matrix(2))

    def test_matrix_power_positive(self):
        A = [[2, 0], [0, 2]]
        self.assertEqual(matrix_power(A, 3), [[8, 0], [0, 8]])

    def test_matrix_power_not_square(self):
        self.assertIsNone(matrix_power([[1, 2, 3]], 2))

    def test_matrix_power_negative(self):
        self.assertIsNone(matrix_power([[1, 2], [3, 4]], -1))

    def test_is_symmetric_true(self):
        A = [[1, 2], [2, 1]]
        self.assertTrue(is_symmetric(A))

    def test_is_symmetric_false(self):
        A = [[1, 0], [1, 1]]
        self.assertFalse(is_symmetric(A))

    def test_is_symmetric_invalid(self):
        self.assertFalse(is_symmetric([1, 2, 3]))

    def test_identity_matrix_valid(self):
        self.assertEqual(identity_matrix(3), [[1,0,0],[0,1,0],[0,0,1]])

    def test_identity_matrix_zero(self):
        self.assertEqual(identity_matrix(0), [])

    def test_matrix_trace_valid(self):
        A = [[1,2],[3,4]]
        self.assertEqual(matrix_trace(A), 5)

    def test_matrix_trace_invalid(self):
        self.assertIsNone(matrix_trace([1,2]))

    def test_matrix_rank_full(self):
        A = [[1,2],[3,4]]
        self.assertEqual(matrix_rank(A), 2)

    def test_matrix_rank_reduction(self):
        A = [[1, 2], [2, 4]]  # rank 1
        self.assertEqual(matrix_rank(A), 1)

    def test_matrix_rank_invalid(self):
        self.assertIsNone(matrix_rank("x"))


if __name__ == "__main__":
    unittest.main()
