from collections import deque

from binary_search_tree import Node, BinaryTree


def in_order(root: Node) -> Node | None:
    if not root:
        return

    in_order(root.left)
    print(root.value)
    in_order(root.right)


def pre_order(root: Node) -> Node | None:
    if not root:
        return

    print(root.value)
    in_order(root.left)
    in_order(root.right)


def post_order(root: Node) -> Node | None:
    if not root:
        return

    in_order(root.left)
    in_order(root.right)
    print(root.value)


def bfs(root: Node) -> None:
    queue = deque()

    if root:
        queue.append(root)

    level = 0
    while len(queue) > 0:
        print(f"Current level tree is {level}")

        for i in range(len(queue)):
            curr: Node = queue.popleft()
            print(curr.value)

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        level += 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    binary_tree = BinaryTree()
    binary_tree.insert(3, 5, 7, 6, 8, 2, 9, 10)

    print("Traversal In Order: ")
    in_order(binary_tree.root)

    print("Traversal Pre Order: ")
    pre_order(binary_tree.root)

    print("Traversal Post Order: ")
    post_order(binary_tree.root)

    print("Traversal BFS: ")
    bfs(binary_tree.root)
