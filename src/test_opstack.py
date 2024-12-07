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

    def test_opstack_double_op(self):
        stack = Opstack()
        stack.push(1.2)
        stack.push("+")
        stack.push("-")
        self.assertEqual(stack._items[-1], "-")

    def test_opstack_solve_empty(self):
        stack = Opstack()
        self.assertRaises(ValueError, stack.solve)

    def test_opstack_solve_zerodiv(self):
        stack = Opstack()
        stack.push(1.2)
        stack.push("/")
        stack.push(0)
        self.assertRaises(ZeroDivisionError, stack.solve)

    def test_opstack_solve_pushresult(self):
        stack = Opstack()
        stack.push(1.2)
        stack.push("+")
        stack.push(2.3)
        stack.solve()
        self.assertEqual(stack._items[0], 3.5)

    def test_opstack_solve_one_val(self):
        stack = Opstack()
        stack.push(1.2)
        self.assertEqual(stack.solve(), 1.2)

    def test_opstack_solve_one_stored(self):
        stack = Opstack()
        stack.push(1.2)
        self.assertEqual(stack._items[-1], 1.2)

    def test_opstack_solve_one_in(self):
        stack = Opstack()
        stack.push(1.2)
        self.assertEqual(stack.count(), 1)

    def test_opstack_reset(self):
        stack = Opstack()
        stack.push(1.2)
        stack.push("-")
        stack.push(3.1)
        stack.reset()
        self.assertEqual(stack.count(), 1)

    def test_opstack_reset_value(self):
        stack = Opstack()
        stack.push(1.2)
        stack.reset()
        self.assertEqual(stack._items[0], 0)

    def test_opstack_peek_num(self):
        stack = Opstack()
        stack.push(9.3)
        self.assertEqual(stack.peek(), 9.3)

    def test_opstack_peek_str(self):
        stack = Opstack()
        stack.push(9.3)
        stack.push("+")
        self.assertEqual(stack.peek(), "+")

    def test_opstack_peek_count(self):
        stack = Opstack()
        stack.push(9.3)
        stack.push("+")
        stack.peek()
        self.assertEqual(stack.count(), 2)


if __name__ == "__main__":
    unittest.main()