class Stack:
    """
    >>> stack = Stack()
    >>> stack.push(2)
    >>> stack.push(1)
    >>> stack.push(8)
    >>> stack.push(10)
    >>> print(stack)
    2, 1, 8, 10
    >>> stack.pop()
    Pop 10 from stack.
    >>> stack.pop()
    Pop 8 from stack.
    >>> stack.pop()
    Pop 1 from stack.
    >>> stack.pop()
    Pop 2 from stack.
    >>> stack.pop()
    Stack is empty.
    """
    def __init__(self):
        self.items = []

    def __str__(self):
        return ", ".join(map(str, self.items))

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, value: int) -> None:
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            print("Stack is empty.")
            return None

        item = self.items.pop()
        print(f"Pop {item} from stack.")
