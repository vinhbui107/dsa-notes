class ListNode:
    def __init__(self, value: int = 0, next_node=None):
        self.value = value
        self.next = next_node


class MyLinkedList:
    def __init__(self) -> None:
        self.size = 0
        self.head: ListNode = None

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1

        current_node = self.head
        for _ in range(0, index):
            current_node = current_node.next

        return current_node.value

    def addAtHead(self, value: int) -> None:
        self.addAtIndex(index=0, value=value)

    def addAtTail(self, value: int) -> None:
        self.addAtIndex(index=self.size, value=value)

    def addAtIndex(self, index: int, value: int) -> None:
        if index > self.size:
            return

        current_node = self.head
        new_node = ListNode(value=value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            for _ in range(0, index - 1):
                current_node = current_node.next

            new_node.next = current_node.next
            current_node.next = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return -1

        if index == 0:
            self.head = self.head.next
        else:
            current_node = self.head

            for _ in range(0, index - 1):
                current_node = current_node.next

            current_node.next = current_node.next.next

        self.size -= 1

    def print_node(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
        print(">>>>>>>>>>>>>>> \n")


# Your MyLinkedList object will be instantiated and called as such:
myLinkedList = MyLinkedList()
myLinkedList.addAtHead(7)
myLinkedList.addAtHead(2)
myLinkedList.addAtHead(1)
myLinkedList.addAtIndex(3, 0)
myLinkedList.print_node()

myLinkedList.deleteAtIndex(2)
myLinkedList.addAtHead(6)

myLinkedList.addAtTail(4)
myLinkedList.print_node()
print(myLinkedList.get(4))
myLinkedList.addAtHead(4)

myLinkedList.addAtIndex(5, 0)
myLinkedList.addAtHead(6)
