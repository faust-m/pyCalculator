import math

class OpQueue:
    def __init__(self):
        self._items = []

    def enqueue(self, item: float | str) -> None:
        last_type = type(self._peek_back())
        if type(item) == str:
            if last_type == str:
                self._items.pop(0)
            elif last_type == type(None):
                raise ValueError("Operation requires operand")
        else:
            if last_type == float:
                raise ValueError("Invalid queue order")
            item = float(item)
        self._items.insert(0, item)

    def dequeue(self) -> float | str | None:
        if len(self._items) > 0:
            return self._items.pop()
        
    def _peek_back(self) -> float | str | None:
        if len(self._items) > 0:
            return self._items[0]
        
    def _return_val(self, value: float) -> float | int:
        if math.isclose(0, value - int(value)):
            return int(value)
        return value

    def solve(self) -> float | int:
        if len(self._items) == 0:
            raise ValueError("No operands in queue")
        elif len(self._items) == 1:
            return self._return_val(self._items[0])
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
        return self._return_val(result)
        