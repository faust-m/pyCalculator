import math
from typing import Any


class Stack:
    def __init__(self) -> None:
        self._items = []

    def push(self, item: Any) -> None:
        self._items.append(item)

    def pop(self) -> Any | None:
        if len(self._items) > 0:
            return self._items.pop()

    def count(self) -> int:
        return len(self._items)


class Opstack(Stack):
    def __init__(self) -> None:
        super().__init__()

    def solve(self) -> float:
        r_val = self.pop()
        op = self.pop()
        result = self.pop()
        if not r_val or not op or not result:
            raise ValueError("Stack is empty!")
        match op:
            case "+":
                result += r_val
            case "-":
                result -= r_val
            case "*":
                result *= r_val
            case "/":
                if math.isclose(0, r_val):
                    raise ZeroDivisionError
                result /= r_val
        self.push(result)
        return result