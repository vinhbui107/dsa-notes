class Stack:

    def __init__(self):
        self.items = []

    def __str__(self):
        return ",".join(map(str, self.items))

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


stack = Stack()
stack.push(2)
stack.push(1)
stack.push(8)
stack.push(10)
print(f"Current stack: {stack}")

stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(f"Current stack: {stack}")
