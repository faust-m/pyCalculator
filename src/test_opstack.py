import math
import unittest
from opstack import Opstack, Stack

class TestOpstack(unittest.TestCase):
    def test_empty_stack(self):
        stack = Stack()
        self.assertEqual(stack.count(), 0)

    def test_stack_push(self):
        stack = Stack()
        stack.push(1)
        stack.push(-2)
        self.assertEqual(stack.count(), 2)

    def test_stack_push_order(self):
        stack = Stack()
        stack.push(1)
        stack.push(3)
        self.assertEqual(stack._items[1], 3)

    def test_stack_pop(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.pop(), 1)

    def test_stack_pop_empty(self):
        stack = Stack()
        stack.pop()
        self.assertEqual(None, None)

    def test_opstack_solve_empty(self):
        stack = Opstack()
        self.assertRaises(ValueError, stack.solve)

    def test_opstack_solve_zerodiv(self):
        stack = Opstack()
        stack.push(1.2)
        stack.push("/")
        stack.push(0)
        self.assertRaises(ZeroDivisionError, stack.solve)


if __name__ == "__main__":
    unittest.main()