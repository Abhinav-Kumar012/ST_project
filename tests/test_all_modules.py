import unittest
from src import matrix_ops, graph_algos, sorting_algos, stats_lib, geometry, set_ops

class TestMatrixOps(unittest.TestCase):
    def test_matrix_add(self):
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        expected = [[6, 8], [10, 12]]
        self.assertEqual(matrix_ops.matrix_add(A, B), expected)

    def test_matrix_mul(self):
        A = [[1, 2], [3, 4]]
        B = [[2, 0], [1, 2]]
        expected = [[4, 4], [10, 8]]
        self.assertEqual(matrix_ops.matrix_mul(A, B), expected)

    def test_matrix_determinant(self):
        A = [[1, 2], [3, 4]]
        self.assertEqual(matrix_ops.matrix_determinant(A), -2)

class TestGraphAlgos(unittest.TestCase):
    def setUp(self):
        self.g = graph_algos.Graph()
        self.g.add_edge(0, 1, 4)
        self.g.add_edge(0, 2, 1)
        self.g.add_edge(2, 1, 2)
        self.g.add_edge(1, 3, 1)
        self.g.add_edge(2, 3, 5)

    def test_dijkstra(self):
        dists = self.g.dijkstra(0)
        self.assertEqual(dists[0], 0)
        self.assertEqual(dists[1], 3) # 0->2->1 (1+2=3) vs 0->1 (4)
        self.assertEqual(dists[3], 4) # 0->2->1->3 (1+2+1=4)

    def test_bfs(self):
        traversal = self.g.bfs(0)
        self.assertTrue(len(traversal) > 0)
        self.assertEqual(traversal[0], 0)

class TestSortingAlgos(unittest.TestCase):
    def test_quick_sort(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        sorted_arr = sorting_algos.quick_sort(arr)
        self.assertEqual(sorted_arr, sorted(arr))

    def test_merge_sort(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        sorted_arr = sorting_algos.merge_sort(arr)
        self.assertEqual(sorted_arr, sorted(arr))

class TestStatsLib(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(stats_lib.mean([1, 2, 3, 4, 5]), 3)

    def test_variance(self):
        self.assertAlmostEqual(stats_lib.variance([1, 2, 3], population=True), 0.666666, places=5)

class TestGeometry(unittest.TestCase):
    def test_distance(self):
        p1 = geometry.Point2D(0, 0)
        p2 = geometry.Point2D(3, 4)
        self.assertEqual(p1.distance_to(p2), 5)

    def test_area_circle(self):
        self.assertAlmostEqual(geometry.area_circle(1), 3.14159, places=5)

class TestSetOps(unittest.TestCase):
    def test_union(self):
        self.assertEqual(sorted(set_ops.set_union([1, 2], [2, 3])), [1, 2, 3])

    def test_intersection(self):
        self.assertEqual(set_ops.set_intersection([1, 2], [2, 3]), [2])

    def test_power_set(self):
        ps = set_ops.power_set([1, 2])
        self.assertEqual(len(ps), 4)

if __name__ == '__main__':
    unittest.main()
