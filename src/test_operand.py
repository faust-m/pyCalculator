import unittest
from operand import Operand

class TestOperand(unittest.TestCase):
    def test_addition(self):
        op1 = Operand(-1)
        op2 = Operand(4)
        result = op1 + op2
        self.assertEqual(result.value, 3)

    
    def test_subtraction(self):
        op1 = Operand(2)
        op2 = Operand(4)
        result = op1 - op2
        self.assertEqual(result.value, -2)


    def test_multiplication(self):
        op1 = Operand(1.5)
        op2 = Operand(2)
        result = op1 * op2
        self.assertEqual(result.value, 3)


    def test_valid_division(self):
        op1 = Operand(4)
        op2 = Operand(2)
        result = op1 / op2
        self.assertEqual(result.value, 2)

    
    def test_invalid_division(self):
        op1 = Operand(4)
        op2 = Operand(0)
        self.assertRaises(ZeroDivisionError, op1.__truediv__, op2)


    def test_create_operand_str(self):
        op = Operand("-21.243")
        self.assertEqual(op.value, -21.243)


    def test_create_operand_point(self):
        op = Operand("2151.")
        self.assertEqual(op.value, 2151)


    def test_update(self):
        op = Operand(215.2)
        op.update(-1.0)
        self.assertEqual(op.value, -1)


if __name__ == "__main__":
    unittest.main()