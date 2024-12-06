from __future__ import annotations
import math

class Operand:
    def __init__(self, value=0.0) -> None:
        self.value = value
    

    def __add__(self, other: Operand) -> Operand:
        return Operand(self.value + other.value)


    def __mul__(self, other: Operand) -> Operand:
        return Operand(self.value * other.value)


    def __sub__(self, other: Operand) -> Operand:
        return Operand(self.value - other.value)


    def __truediv__(self, other: Operand) -> Operand:
        if math.isclose(0.0, other.value):
            raise ZeroDivisionError()
        return Operand(self.value / other.value)
