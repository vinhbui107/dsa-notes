class Queue:
    """
    >>> queue = Queue()
    >>> queue.enqueue(1)
    >>> queue.enqueue(2)
    >>> queue.enqueue(3)
    >>> queue.enqueue(4)
    >>> queue.enqueue(5)
    >>> print(queue)
    1, 2, 3, 4, 5
    >>> queue.dequeue()
    Get 1 from queue.
    >>> queue.dequeue()
    Get 2 from queue.
    >>> queue.dequeue()
    Get 3 from queue.
    >>> queue.dequeue()
    Get 4 from queue.
    >>> queue.dequeue()
    Get 5 from queue.
    >>> queue.dequeue()
    Queue is empty.
    """
    def __init__(self):
        self.items = []

    def __str__(self):
        return ", ".join(map(str, self.items))

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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
