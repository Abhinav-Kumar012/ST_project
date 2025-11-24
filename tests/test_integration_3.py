import unittest
from src import integration_3


class TestIntegration3(unittest.TestCase):
    def test_graph_matrix_analysis(self):
        edges = [(0, 1, 1), (0, 2, 1), (1, 3, 1), (2, 3, 1), (0, 3, 5)]

        dist, is_prime, adj_sq = integration_3.graph_matrix_analysis(edges, 0, 3)

        self.assertEqual(dist, 2)
        self.assertFalse(is_prime)
        self.assertEqual(
            adj_sq, [[0, 0, 0, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        )

    def test_graph_matrix_analysis_with_common(self):
        edges = [(0, 2, 1), (0, 3, 1), (1, 2, 1), (1, 3, 1)]

        dist, is_prime, adj_sq = integration_3.graph_matrix_analysis(edges, 0, 1)

        self.assertEqual(dist, float("inf"))
        self.assertTrue(is_prime)
        self.assertEqual(
            adj_sq, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        )

    def test_v2(self):
        edges = [(0, 1, 2), (1, 2, 3), (0, 2, -10)]

        dist, is_prime, adj_sq = integration_3.graph_matrix_analysis(edges, 0, 2)

        self.assertEqual(dist, 5)
        self.assertFalse(is_prime)
        self.assertEqual(adj_sq, [[0, 0, 6], [0, 0, 0], [0, 0, 0]])

    def test_empty_graph(self):
        edges = []

        dist, is_prime, adj_sq = integration_3.graph_matrix_analysis(edges, 0, 2)

        self.assertEqual(dist, float("inf"))
        self.assertFalse(is_prime)
        self.assertEqual(adj_sq, [[0]])


if __name__ == "__main__":
    unittest.main()
