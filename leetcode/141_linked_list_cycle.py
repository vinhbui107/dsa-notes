from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    https://leetcode.com/problems/linked-list-cycle

    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current_node: Optional[ListNode] = head
        slow_node: Optional[ListNode] = head
        steps = 0

        while current_node:
            if steps > 1 and current_node == slow_node:
                return True

            if steps % 2 == 0:
                slow_node = slow_node.next

            steps += 1
            current_node = current_node.next

        return False
