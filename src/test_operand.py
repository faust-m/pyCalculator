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



if __name__ == "__main__":
    unittest.main()