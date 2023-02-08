from __future__ import annotations


class Node:
    def __init__(self, value: int, left: Node = None, right: Node = None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return self._get_js_display(self.root)

    def is_empty(self) -> bool:
        return True if not self.root else False

    def insert(self, value: int) -> None:
        new_node = Node(value=value)

        if self.is_empty():
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if current_node.value == value:
                    print("Error! Duplicated value!")
                    break

                if value < current_node.value:
                    if not current_node.left:
                        current_node.left = new_node
                        break
                    current_node = current_node.left
                else:
                    if not current_node.right:
                        current_node.right = new_node
                        break
                    current_node = current_node.right

    def remove(self, value: int) -> None:
        if self.is_empty():
            return

        current_node = self.root
        parent_node = None
        while current_node:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left

            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right

            # found node we need to delete
            elif value == current_node.value:
                # Case 1: Node does not have a right child
                if not current_node.right:
                    parent_node.left = current_node.left
                # case 2: The right child does not have a left child
                elif not current_node.right.left:
                    parent_node.right = current_node.right
                # case 3: The right child have a left child
                else:
                    min_node = current_node.right.left
                    parent_min_node = current_node.right

                    # find min value in the right subtree
                    while min_node.left:
                        parent_min_node = min_node
                        min_node = min_node.left

                    parent_min_node.left = None
                    min_node.left = current_node.left
                    min_node.right = current_node.right
                    parent_node.right = min_node
                return
            else:
                return

    def count(self, node: Node) -> int:
        if not node:
            return 0

        left_nodes = self.count(node.left)
        right_nodes = self.count(node.right)

        return 1 + left_nodes + right_nodes

    def _display(self, node: Node) -> dict | None:
        tree = {
            "value": node.value,
            "left": None if not node.left else self._display(node.left),
            "right": None if not node.right else self._display(node.right)
        }

        return tree

    def _get_js_display(self, node: Node) -> str:
        tree = self._display(node)
        return str(tree).replace("None", "null")


binary_tree = BinaryTree()
binary_tree.insert(30)
binary_tree.insert(25)
binary_tree.insert(35)
binary_tree.insert(15)
binary_tree.insert(21)
binary_tree.insert(23)
binary_tree.insert(22)
binary_tree.insert(24)
binary_tree.insert(19)
binary_tree.insert(40)
binary_tree.insert(45)
print(f"Current tree is: {binary_tree.__str__()}")
print(f"Total nodes in tree is: {binary_tree.count(binary_tree.root)}")

binary_tree.remove(21)
print(f"Current tree after remove value 21: {binary_tree.__str__()}")
print(f"Total nodes in tree is: {binary_tree.count(binary_tree.root)}")
