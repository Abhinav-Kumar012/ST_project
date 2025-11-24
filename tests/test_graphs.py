import unittest
from src.graph_algos import *


class TestGraphBasics(unittest.TestCase):
    def test_add_edge(self):
        g = Graph()
        g.add_edge("A", "B", 5)
        self.assertIn("A", g.adj_list)
        self.assertIn("B", g.adj_list)
        self.assertEqual(g.adj_list["A"], [("B", 5)])

    def test_bfs(self):
        g = Graph()
        g.add_edge("A", "B")
        g.add_edge("A", "C")
        g.add_edge("B", "D")
        order = g.bfs("A")
        self.assertEqual(order, ["A", "B", "C", "D"])

    def test_bfs_invalid_start(self):
        g = Graph()
        self.assertEqual(g.bfs("Z"), [])

    def test_dfs(self):
        g = Graph()
        g.add_edge("A", "B")
        g.add_edge("A", "C")
        g.add_edge("B", "D")
        order = g.dfs("A")
        self.assertEqual(order, ["A", "B", "D", "C"])

    def test_dfs_invalid_start(self):
        g = Graph()
        self.assertEqual(g.dfs("Z"), [])


class TestShortestPaths(unittest.TestCase):
    def test_dijkstra(self):
        g = Graph()
        g.add_edge("A", "B", 2)
        g.add_edge("A", "C", 5)
        g.add_edge("B", "C", 1)
        dist = g.dijkstra("A")
        self.assertEqual(dist["C"], 3)

    def test_dijkstra_invalid_start(self):
        g = Graph()
        self.assertEqual(g.dijkstra("Z"), {})

    def test_bellman_ford(self):
        g = Graph()
        g.add_edge("A", "B", 1)
        g.add_edge("B", "C", 2)
        dist = g.bellman_ford("A")
        self.assertEqual(dist["C"], 3)

    def test_bellman_ford_negative_cycle(self):
        g = Graph()
        g.add_edge("A", "B", 1)
        g.add_edge("B", "A", -2)
        self.assertIsNone(g.bellman_ford("A"))

    def test_floyd_warshall(self):
        g = Graph()
        g.add_edge("A", "B", 3)
        g.add_edge("B", "C", 4)
        dist = g.floyd_warshall()
        self.assertEqual(dist["A"]["C"], 7)


class TestTopologicalSort(unittest.TestCase):
    def test_topological_sort_valid(self):
        g = Graph()
        g.add_edge("A", "B")
        g.add_edge("B", "C")
        result = g.topological_sort()
        self.assertEqual(result, ["A", "B", "C"])

    def test_topological_sort_with_cycle(self):
        g = Graph()
        g.add_edge("A", "B")
        g.add_edge("B", "A")
        self.assertIsNone(g.topological_sort())


class TestUnionFind(unittest.TestCase):
    def test_find_and_union(self):
        uf = UnionFind(["A", "B", "C"])
        self.assertEqual(uf.find("A"), "A")
        self.assertTrue(uf.union("A", "B"))
        self.assertEqual(uf.find("A"), uf.find("B"))
        self.assertFalse(uf.union("A", "B"))

    def test_union_rank_logic(self):
        uf = UnionFind(["A", "B"])
        uf.rank["A"] = 1
        uf.rank["B"] = 0
        uf.union("A", "B")
        self.assertEqual(uf.find("B"), "A")


class TestKruskal(unittest.TestCase):
    def test_kruskal_mst(self):
        g = Graph()
        g.add_edge("A", "B", 1)
        g.add_edge("A", "C", 2)
        g.add_edge("B", "C", 3)
        mst, total = kruskal_mst(g)
        self.assertEqual(total, 3)
        self.assertEqual(len(mst), 2)


class TestPrim(unittest.TestCase):
    def test_prim_mst(self):
        g = Graph()
        g.add_edge("A", "B", 1)
        g.add_edge("A", "C", 4)
        g.add_edge("B", "C", 2)
        mst, total = prim_mst(g, "A")
        self.assertEqual(total, 3)
        self.assertEqual(len(mst), 2)


class TestCycleDetection(unittest.TestCase):
    def test_has_cycle_true(self):
        g = Graph()
        g.add_edge("A", "B")
        g.add_edge("B", "C")
        g.add_edge("C", "A")
        self.assertTrue(has_cycle(g))

    def test_has_cycle_false(self):
        g = Graph()
        g.add_edge("A", "B")
        g.add_edge("B", "C")
        self.assertFalse(has_cycle(g))


class TestConnectedComponents(unittest.TestCase):
    def test_connected_components(self):
        g = Graph()
        g.add_edge("A", "B")
        g.add_edge("C", "D")
        comps = find_connected_components(g)
        sorted_comps = [sorted(c) for c in comps]
        self.assertIn(["A", "B"], sorted_comps)
        self.assertIn(["C", "D"], sorted_comps)


if __name__ == "__main__":
    unittest.main()
