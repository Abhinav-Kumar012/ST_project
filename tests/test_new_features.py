import unittest
import math
from src.banking import Transaction, SavingsAccount, CheckingAccount, Bank, Account
from src.geometry import Rectangle, Circle, Line, Point2D, Point3D
from src.graph_algos import Graph, prim_mst, has_cycle, find_connected_components
from src.matrix_ops import matrix_inverse, matrix_power, is_symmetric, identity_matrix
from src.stats_lib import z_score, percentile, iqr, skewness, kurtosis
from src.data_structures import LinkedList, Stack, Queue, BinarySearchTree
from src.string_utils import is_palindrome, is_anagram, levenshtein_distance, to_camel_case, to_snake_case
from src.search_algos import linear_search, binary_search, jump_search, exponential_search

class TestBankingFeatures(unittest.TestCase):
    def test_transaction_history(self):
        acc = Account(100)
        acc.deposit(50)
        acc.withdraw(30)
        history = acc.get_transaction_history()
        self.assertEqual(len(history), 2)
        self.assertEqual(history[0].type, "DEPOSIT")
        self.assertEqual(history[1].type, "WITHDRAWAL")

    def test_savings_account(self):
        sav = SavingsAccount(100, 0.1)
        sav.apply_interest()
        self.assertEqual(sav.get_balance(), 110)
        self.assertEqual(sav.get_transaction_history()[-1].type, "INTEREST")

    def test_checking_account(self):
        chk = CheckingAccount(100, 50)
        self.assertTrue(chk.withdraw(140))
        self.assertEqual(chk.get_balance(), -40)
        self.assertFalse(chk.withdraw(20)) # Exceeds overdraft

class TestGeometryFeatures(unittest.TestCase):
    def test_rectangle(self):
        rect = Rectangle(Point2D(0, 10), 10, 5)
        self.assertEqual(rect.area(), 50)
        self.assertEqual(rect.perimeter(), 30)
        self.assertTrue(rect.contains(Point2D(5, 8)))
        self.assertFalse(rect.contains(Point2D(11, 8)))

    def test_circle(self):
        circ = Circle(Point2D(0, 0), 5)
        self.assertAlmostEqual(circ.area(), math.pi * 25)
        self.assertTrue(circ.contains(Point2D(3, 4)))
        self.assertFalse(circ.contains(Point2D(6, 0)))

    def test_line(self):
        l = Line(Point2D(0, 0), Point2D(4, 4))
        self.assertEqual(l.slope(), 1)
        self.assertEqual(l.y_intercept(), 0)

class TestGraphFeatures(unittest.TestCase):
    def setUp(self):
        self.g = Graph()
        self.g.add_edge('A', 'B', 1)
        self.g.add_edge('B', 'C', 2)
        self.g.add_edge('C', 'A', 3) # Cycle
        self.g.add_edge('D', 'E', 4) # Disconnected

    def test_has_cycle(self):
        self.assertTrue(has_cycle(self.g))
        
    def test_connected_components(self):
        components = find_connected_components(self.g)
        self.assertEqual(len(components), 2)

    def test_prim_mst(self):
        g2 = Graph()
        g2.add_edge('A', 'B', 2)
        g2.add_edge('B', 'C', 3)
        g2.add_edge('A', 'C', 1) # A-C is cheaper
        # Prim's should pick A-C (1) and A-B (2) -> Total 3
        # Wait, A-C(1), then from C or A... C-B(3) vs A-B(2). A-B is cheaper.
        # MST: A-C, A-B. Weight 3.
        mst, weight = prim_mst(g2, 'A')
        self.assertEqual(weight, 3)

class TestMatrixFeatures(unittest.TestCase):
    def test_matrix_power(self):
        A = [[1, 0], [0, 1]]
        res = matrix_power(A, 5)
        self.assertEqual(res, A)
        
        B = [[2, 0], [0, 2]]
        res_b = matrix_power(B, 2)
        self.assertEqual(res_b, [[4, 0], [0, 4]])

    def test_is_symmetric(self):
        self.assertTrue(is_symmetric([[1, 2], [2, 1]]))
        self.assertFalse(is_symmetric([[1, 2], [3, 1]]))

class TestStatsFeatures(unittest.TestCase):
    def test_z_score(self):
        data = [1, 2, 3, 4, 5]
        # Mean = 3, StdDev (pop) = sqrt(2) ~= 1.414
        z = z_score(data, 3)
        self.assertEqual(z, 0)

    def test_percentile(self):
        data = [15, 20, 35, 40, 50]
        p = percentile(data, 50) # Median
        self.assertEqual(p, 35)

class TestDataStructures(unittest.TestCase):
    def test_linked_list(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        self.assertTrue(ll.find(1))
        self.assertFalse(ll.find(3))
        ll.reverse()
        self.assertEqual(str(ll), "2 -> 1")

    def test_stack_queue(self):
        s = Stack()
        s.push(1)
        self.assertEqual(s.pop(), 1)
        
        q = Queue()
        q.enqueue(1)
        self.assertEqual(q.dequeue(), 1)

class TestStringUtils(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("hello"))

    def test_anagram(self):
        self.assertTrue(is_anagram("listen", "silent"))

    def test_camel_snake(self):
        self.assertEqual(to_camel_case("hello_world"), "helloWorld")
        self.assertEqual(to_snake_case("helloWorld"), "hello_world")

class TestSearchAlgos(unittest.TestCase):
    def test_searches(self):
        arr = [1, 3, 5, 7, 9, 11]
        self.assertEqual(linear_search(arr, 5), 2)
        self.assertEqual(binary_search(arr, 5), 2)
        self.assertEqual(jump_search(arr, 5), 2)
        self.assertEqual(exponential_search(arr, 5), 2)
        self.assertEqual(binary_search(arr, 6), -1)

if __name__ == '__main__':
    unittest.main()
