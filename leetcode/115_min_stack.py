class MinStack:
    """
    https://leetcode.com/problems/min-stack/

    >>> stack = MinStack()
    >>> stack.push(2147483646)
    >>> stack.push(2147483646)
    >>> stack.push(2147483647)
    >>> stack.top()
    2147483647
    >>> stack.pop()
    >>> stack.getMin()
    2147483646
    >>> stack.pop()
    >>> stack.getMin()
    2147483646
    >>> stack.pop()
    >>> stack.push(2147483647)
    >>> stack.top()
    2147483647
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
