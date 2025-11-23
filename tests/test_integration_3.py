import unittest
from src import integration_3

class TestIntegration3(unittest.TestCase):
    def test_graph_matrix_analysis(self):
        # Graph:
        # 0 -> 1 (1)
        # 0 -> 2 (1)
        # 1 -> 3 (1)
        # 2 -> 3 (1)
        # 0 -> 3 (5)
        
        edges = [
            (0, 1, 1),
            (0, 2, 1),
            (1, 3, 1),
            (2, 3, 1),
            (0, 3, 5)
        ]
        
        # Shortest path 0 -> 3:
        # 0->1->3 (cost 2)
        # 0->2->3 (cost 2)
        # 0->3 (cost 5)
        # Min is 2.
        
        # Common neighbors of 0 and 3?
        # Neighbors of 0: [1, 2, 3]
        # Neighbors of 3: [] (It's directed, 3 has no outgoing edges in this list)
        # Intersection: []
        # Count: 0
        # is_prime(0) -> False
        
        # Wait, let's make it interesting so common neighbors exist.
        # Let's check common neighbors of 0 and some other node?
        # Or make edges bidirectional? The graph implementation is directed.
        # Let's adjust the test expectation.
        
        dist, is_prime = integration_3.graph_matrix_analysis(edges, 0, 3)
        
        self.assertEqual(dist, 2)
        self.assertFalse(is_prime) # 0 is not prime

    def test_graph_matrix_analysis_with_common(self):
        # 0 -> 1
        # 0 -> 2
        # 1 -> 3
        # 2 -> 3
        # Let's check common neighbors of 0 and 3 if we add back edges?
        # Or let's check common neighbors of two nodes that actually share a target?
        # No, the function checks neighbors OF start and end.
        # If start=0, neighbors=[1, 2]
        # If end=0, neighbors=[]
        
        # Let's try a case where we check common neighbors of two source nodes?
        # But the function signature is (edges, start, end).
        
        # Let's just trust the logic:
        # 0 -> 2
        # 1 -> 2
        # Neighbors of 0: [2]
        # Neighbors of 1: [2]
        # Common: [2] (Size 1) -> Not prime.
        
        # 0 -> 2, 0 -> 3
        # 1 -> 2, 1 -> 3
        # Neighbors 0: [2, 3]
        # Neighbors 1: [2, 3]
        # Common: [2, 3] (Size 2) -> Prime!
        
        edges = [
            (0, 2, 1), (0, 3, 1),
            (1, 2, 1), (1, 3, 1)
        ]
        
        # We need to pass start=0, end=1 to check their common neighbors.
        # But we also need shortest path from 0 to 1.
        # 0 to 1: No path. Dist = inf.
        
        dist, is_prime = integration_3.graph_matrix_analysis(edges, 0, 1)
        
        self.assertEqual(dist, float('inf'))
        self.assertTrue(is_prime) # 2 is prime

if __name__ == '__main__':
    unittest.main()
