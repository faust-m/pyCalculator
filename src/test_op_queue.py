import math
import unittest
from op_queue import OpQueue

class TestOpQueue(unittest.TestCase):

    def test_enqueue_first_in(self):
        q = OpQueue()
        q.enqueue(2)
        q.enqueue("+")
        self.assertEqual(q._items[1], 2)

    def test_enqueue_last_in(self):
        q = OpQueue()
        q.enqueue(2)
        q.enqueue("+")
        self.assertEqual(q._items[0], "+")

    def test_enqueue_consec_ops(self):
        q = OpQueue()
        q.enqueue(2)
        q.enqueue("+")
        q.enqueue("-")
        self.assertTrue("+" not in q._items and "-" in q._items)

    def test_enqueue_consec_nums(self):
        q = OpQueue()
        q.enqueue(2)
        self.assertRaises(ValueError, q.enqueue, 4)

    def test_enqueue_op_first(self):
        q = OpQueue()
        self.assertRaises(ValueError, q.enqueue, "+")

    def test_dequeue(self):
        q = OpQueue()
        q.enqueue(2)
        q.enqueue("+")
        q.enqueue(5)
        self.assertEqual(q.dequeue(), 7)

    def test_dequeue_empty(self):
        q = OpQueue()
        self.assertEqual(q.dequeue(), None)

    def test_count_empty(self):
        q = OpQueue()
        self.assertEqual(q.count(), 0)

    def test_count(self):
        q = OpQueue()
        q.enqueue(1)
        q.enqueue("+")
        self.assertEqual(q.count(), 2)

    def test_solve_empty(self):
        q = OpQueue()
        self.assertRaises(ValueError, q.solve)

    def test_solve_add(self):
        q = OpQueue()
        q.enqueue(1.2)
        q.enqueue("+")
        q.enqueue(2.4)
        self.assertTrue(math.isclose(3.6, q._items[0]))

    def test_solve_subtract(self):
        q = OpQueue()
        q.enqueue(1.2)
        q.enqueue("-")
        q.enqueue(2.4)
        self.assertTrue(math.isclose(-1.2, q._items[0]))

    def test_solve_multiply(self):
        q = OpQueue()
        q.enqueue(1.2)
        q.enqueue("*")
        q.enqueue(3)
        self.assertTrue(math.isclose(3.6, q._items[0]))

    def test_solve_divide(self):
        q = OpQueue()
        q.enqueue(4.2)
        q.enqueue("/")
        q.enqueue(2)
        self.assertTrue(math.isclose(2.1, q._items[0]))

    def test_solve_divide_by_zero(self):
        q = OpQueue()
        q.enqueue(4.2)
        q.enqueue("/")
        self.assertRaises(ZeroDivisionError, q.enqueue, 0)


if __name__ == "__main__":
    unittest.main()