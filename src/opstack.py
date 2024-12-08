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

    def push(self, item: float | str) -> None:
        if type(item) == str and type(self.peek()) == str:
            self.pop()
        super().push(item)

    def solve(self) -> float:
        r_val = self.pop()
        op = self.pop()
        l_val = self.pop()
        if l_val == None or op == None:
            if r_val == None:
                raise ValueError("Stack is empty!")
            result = r_val
        match op:
            case "+":
                result = l_val + r_val
            case "-":
                result = l_val - r_val
            case "*":
                result = l_val * r_val
            case "/":
                if math.isclose(0, r_val):
                    raise ZeroDivisionError()
                result = 1.0 * l_val / r_val
        self.push(result)
        if math.isclose(int(result), result):
            return int(result)
        return result
    
    def reset(self) -> None:
        self._items.clear()

    def peek(self) -> float | str | None:
        if self.count() > 0:
            return self._items[-1]