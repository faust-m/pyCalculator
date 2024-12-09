import math

class OpQueue:
    def __init__(self):
        self._items = []

    def count(self) -> int:
        return len(self._items)

    def enqueue(self, item: float | str) -> None:
        last_type = type(self._peek_back())
        if type(item) == str:
            if last_type == str:
                self._items.pop(0)
            elif last_type == type(None):
                raise ValueError("Operation requires operand")
            self._items.insert(0, item)
        else:
            if last_type == float:
                raise ValueError("Invalid queue order")
            self._items.insert(0, float(item))
            if self.count() == 3:
                self.solve()

    def dequeue(self) -> float | str | None:
        if len(self._items) > 0:
            return self._items.pop()
        
    def clear(self) -> None:
        self._items.clear()
        
    def _peek_back(self) -> float | str | None:
        if len(self._items) > 0:
            return self._items[0]

    def solve(self) -> None:
        if len(self._items) == 0:
            raise ValueError("No operands in queue")
        result = self.dequeue()
        match self.dequeue():
            case "+":
                result += self.dequeue()
            case "-":
                result -= self.dequeue()
            case "*":
                result *= self.dequeue()
            case "/":
                r_val = self.dequeue()
                if math.isclose(0, r_val):
                    raise ZeroDivisionError()
                result /= r_val
        self.enqueue(result)
        