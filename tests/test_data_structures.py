import unittest
from src.data_structures import LinkedList, Stack, Queue, BinarySearchTree


class TestLinkedList(unittest.TestCase):
    def test_append(self):
        ll = LinkedList()
        ll.append(10)
        self.assertEqual(str(ll), "10")

        ll.append(20)
        self.assertEqual(str(ll), "10 -> 20")

    def test_prepend(self):
        ll = LinkedList()
        ll.prepend(10)
        self.assertEqual(str(ll), "10")

        ll.prepend(5)
        self.assertEqual(str(ll), "5 -> 10")

    def test_delete(self):
        ll = LinkedList()

        ll.delete(5)

        ll.append(10)
        ll.append(20)
        ll.delete(10)
        self.assertEqual(str(ll), "20")

        ll.append(30)
        ll.append(40)
        ll.delete(30)
        self.assertEqual(str(ll), "20 -> 40")

        ll.delete(999)
        self.assertEqual(str(ll), "20 -> 40")

    def test_find(self):
        ll = LinkedList()
        self.assertFalse(ll.find(5))

        ll.append(10)
        ll.append(20)
        self.assertTrue(ll.find(10))
        self.assertTrue(ll.find(20))
        self.assertFalse(ll.find(30))

    def test_reverse(self):
        ll = LinkedList()
        ll.reverse()
        self.assertEqual(str(ll), "")

        ll.append(10)
        ll.reverse()
        self.assertEqual(str(ll), "10")

        ll.append(20)
        ll.append(30)
        ll.reverse()
        self.assertEqual(str(ll), "30 -> 20 -> 10")


class TestStack(unittest.TestCase):
    def test_push_pop_peek(self):
        s = Stack()
        self.assertTrue(s.is_empty())

        self.assertIsNone(s.pop())
        self.assertIsNone(s.peek())

        s.push(10)
        s.push(20)
        self.assertEqual(s.peek(), 20)
        self.assertEqual(s.pop(), 20)
        self.assertEqual(s.pop(), 10)
        self.assertIsNone(s.pop())


class TestQueue(unittest.TestCase):
    def test_enqueue_dequeue_peek(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        self.assertIsNone(q.dequeue())
        self.assertIsNone(q.peek())

        q.enqueue(10)
        q.enqueue(20)
        self.assertEqual(q.peek(), 10)
        self.assertEqual(q.dequeue(), 10)
        self.assertEqual(q.dequeue(), 20)
        self.assertIsNone(q.dequeue())


class TestBinarySearchTree(unittest.TestCase):
    def test_insert_and_search(self):
        bst = BinarySearchTree()

        self.assertFalse(bst.search(10))

        bst.insert(10)
        self.assertTrue(bst.search(10))

        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(12)

        self.assertTrue(bst.search(5))
        self.assertTrue(bst.search(15))
        self.assertTrue(bst.search(3))
        self.assertTrue(bst.search(12))
        self.assertFalse(bst.search(99))

    def test_traversals(self):
        bst = BinarySearchTree()
        for x in [10, 5, 15]:
            bst.insert(x)

        self.assertEqual(bst.inorder_traversal(), [5, 10, 15])
        self.assertEqual(bst.preorder_traversal(), [10, 5, 15])
        self.assertEqual(bst.postorder_traversal(), [5, 15, 10])


if __name__ == "__main__":
    unittest.main()
