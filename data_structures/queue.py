class Queue:

    def __init__(self):
        self.items = []

    def __str__(self):
        return ",".join(map(str, self.items))

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
            return None

        item = self.items.pop(0)
        print(f"Get {item} from queue.")


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(f"Current queue: {queue}")

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
print(f"Current queue: {queue}")
