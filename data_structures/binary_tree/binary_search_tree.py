from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None
    parent: Node | None = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.__display(self.root))

    def __insert(self, value: int) -> None:
        new_node = Node(value)

        if self.is_empty():
            self.root = new_node
            return

        current_node = self.root
        while True:
            if current_node.value == value:
                print("Error! Duplicated value!")
                break

            if value < current_node.value:
                if not current_node.left:
                    current_node.left = new_node
                    break
                else:
                    current_node = current_node.left
            else:
                if not current_node.right:
                    current_node.right = new_node
                    break
                else:
                    current_node = current_node.right

    def __search(self, value: int) -> [Node, Node | None]:
        if self.is_empty():
            raise IndexError("Warning: Tree is empty! please use another.")

        node = self.root
        parent_node = None
        while node is not None and node.value is not value:
            parent_node = node
            node = node.left if value < node.value else node.right

        return node, parent_node

    def __display(self, node: Node) -> dict | None:
        if self.is_empty():
            raise IndexError("Warning: Tree is empty! please use another.")

        return {
            "value": node.value,
            "left": None if not node.left else self.__display(node.left),
            "right": None if not node.right else self.__display(node.right)
        }

    def is_empty(self) -> bool:
        return True if not self.root else False

    def count(self, node: Node) -> int:
        if not node:
            return 0

        left_nodes = self.count(node.left)
        right_nodes = self.count(node.right)

        return 1 + left_nodes + right_nodes

    def insert(self, *values):
        for value in values:
            self.__insert(value)

    def remove(self, root: Node | None, value: int) -> Node | None:
        if not root:
            return root

        if value > root.value:
            root.right = self.remove(root.right, value)
        elif value < root.value:
            root.left = self.remove(root.left, value)
        else:
            if not root.left:  # has right
                return root.right
            elif not root.right:  # has left
                return root.left

            # find min
            current = root.right
            while current.left:
                current = current.left

            root.value = current.value
            root.right = self.remove(root.right, root.value)

        return root


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    binary_tree = BinaryTree()
    binary_tree.insert(3, 5, 7, 6, 8, 2, 9, 10)
    print(f"Current tree is: {binary_tree.__str__()}")
    print(f"Total nodes in tree is: {binary_tree.count(binary_tree.root)}")

    binary_tree.remove(binary_tree.root, 3)
    print(f"Current tree after remove value 3: {binary_tree.__str__()}")
    print(f"Total nodes in tree is: {binary_tree.count(binary_tree.root)}")
