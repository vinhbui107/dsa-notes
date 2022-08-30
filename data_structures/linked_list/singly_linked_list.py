from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, next_node: ListNode = None, value: int = None):
        self.next_node = next_node
        self.value = value


class SinglyLinkedList:
    def __init__(self):
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

        if self.is_empty():
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
        new_node = ListNode(value=value)

        if not self.head:
            self.head = new_node
        else:
            current_node = self.head

            while current_node and current_node.next_node:
                current_node = current_node.next_node

            current_node.next_node = new_node

    def prepend(self, value: int) -> None:
        """Add an element at the beginning of the list."""
        new_node = ListNode(value=value)
        new_node.next_node = self.head
        self.head = new_node

    def pop(self) -> None:
        """Remove an element at the end of the list"""
        if self.is_empty():
            return

        current_node = self.head

        while current_node.next_node and current_node.next_node.next_node:
            current_node = current_node.next_node

        current_node.next_node = None

    def pop_first(self) -> None:
        """Remove the first element of the list"""
        if self.is_empty():
            return

        self.head = self.head.next_node

    def remove(self, index: int) -> None:
        """Remove the element at a specified location from a non-empty list."""
        if self.is_empty():
            return

        if index == 0:
            self.pop_first()
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next_node

            current_node.next_node = current_node.next_node.next_node

    def reverse(self):
        """Reverse list"""
        current_node = self.head
        prev_node = None

        while current_node:
            next_node = current_node.next_node
            current_node.next_node = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node


linked_list = SinglyLinkedList()
linked_list.prepend(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
print(f"After append list: {linked_list}")
print(f"Value at index 1: {linked_list.get(1)}")

linked_list.pop()
print(f"Current list after remove tail node: {linked_list}")

linked_list.pop_first()
print(f"Current list after remove head node: {linked_list}")

linked_list.remove(1)
print(f"Current list after remove index 1: {linked_list}")

linked_list.prepend(1)
linked_list.append(3)
linked_list.append(4)
print(f"Current list: {linked_list}")

linked_list.reverse()
print(f"List after reverse {linked_list}")
