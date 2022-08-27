from typing import Optional


class ListNode:
    def __init__(self, value: int, next_node=None, previous_node=None):
        self.value = value
        self.next_node = next_node
        self.previous_node = previous_node


class DoubleLinkedList:
    def __init__(self):
        self.size = 0
        self.head: Optional[ListNode] = None

    def __str__(self):
        values = []
        current_node = self.head

        while current_node:
            values.append(current_node.value)
            current_node = current_node.next_node

        return ",".join(map(str, values))

    def get(self, index: int) -> int:
        """Return an element from the list at any given position."""

        if not self.is_empty():
            return -1

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next_node

        return current_node.value

    def is_empty(self) -> bool:
        """Return true if the list is empty, otherwise return false."""
        return True if not self.head else False

    def append(self, value: int) -> None:
        """Add an element at the end of the list."""

    def prepend(self, value: int) -> None:
        """Add an element at the beginning of the list."""

    def pop(self) -> None:
        """Remove an element at the end of the list"""

    def pop_first(self) -> None:
        """Remove the first element of the list"""

    def remove(self, index: int, value: int) -> None:
        """Remove the element at a specified location from a non-empty list."""
