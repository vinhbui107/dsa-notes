from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find a mid node in the linked list
        mid_node = self.find_mid_node(head)

        # reverse the part from mid node to end of the linked list
        second = self.reverse_linked_list(mid_node)

        # merge 2 array
        first = head
        mid_node.next = None  # this for help break the loop below

        while first.next and second.next:
            next_first_node = first.next
            next_second_node = second.next

            first.next = second
            second.next = next_first_node

            first = next_first_node
            second = next_second_node

    def find_mid_node(self, head: Optional[ListNode]):
        fast, slow = head, head
        steps = 0

        while fast.next != None:
            if steps % 2 == 0:
                slow = slow.next
            fast = fast.next
            steps += 1

        return slow

    def reverse_linked_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        current_node = head

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        return prev_node
