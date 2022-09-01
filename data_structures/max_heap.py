class MaxHeap:
    """
    >>> max_heap = MaxHeap()
    >>> max_heap.insert(6)
    >>> max_heap.insert(10)
    >>> max_heap.insert(15)
    >>> max_heap.insert(12)
    >>> print(max_heap)
    15, 12, 10, 6
    >>> len(max_heap)
    4
    >>> max_heap.extract_max()
    15
    >>> max_heap.extract_max()
    12
    >>> max_heap.extract_max()
    10
    >>> max_heap.extract_max()
    6
    >>> max_heap.extract_max()
    Heap is empty.
    -1
    """

    def __init__(self):
        self.heap = [0]
        self.size = 0

    def __str__(self):
        return ", ".join(map(str, self.heap[1:]))

    def __len__(self):
        return self.size

    @staticmethod
    def _get_get_parent(pos: int) -> int:
        return pos // 2

    @staticmethod
    def _get_left_child(pos: int) -> int:
        return pos * 2

    @staticmethod
    def _get_right_child(pos: int) -> int:
        return pos * 2 + 1

    def __swap_up(self, pos: int):
        temp = self.heap[pos]

        while pos // 2 > 0:
            parent = self._get_get_parent(pos)
            if self.heap[pos] > self.heap[parent]:
                # swap data with parent node
                self.heap[pos] = self.heap[parent]
                self.heap[parent] = temp

            pos //= 2

    def __swap_down(self, pos: int):
        while self.size >= 2 * pos:
            left_child = self._get_left_child(pos)
            right_child = self._get_right_child(pos)

            if right_child > self.size:
                bigger_child = 2 * pos
            else:
                if self.heap[left_child] > self.heap[right_child]:
                    bigger_child = 2 * pos
                else:
                    bigger_child = 2 * pos + 1

            temp = self.heap[pos]
            if self.heap[pos] < self.heap[bigger_child]:
                self.heap[pos] = self.heap[bigger_child]
                self.heap[bigger_child] = temp

            pos = bigger_child

    def insert(self, value: int) -> None:
        self.heap.append(value)
        self.size += 1
        self.__swap_up(self.size)

    def max(self) -> int:
        if not self.size:
            print("Heap is empty.")
            return -1

        return self.heap[1]

    def extract_max(self) -> int:
        if not self.size:
            print("Heap is empty.")
            return -1

        max_value = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.__swap_down(1)
        return max_value

