
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    https://leetcode.com/problems/reverse-linked-list/

    """
    def reverseList(self, head: list[ListNode]) -> list[ListNode]:
        # a -> b -> c -> d -> null
        # prev_node = null
        # curr_node = a

        # first loop
        # we want to make like this null <- a <- b
        # next_node = b -> c -> d -> null
        # cur_node.next = null
        # prev_node = a -> nul
        # curr_node = a -> c -> d -> null
        prev_node = None
        cur_node = head

        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node

        return prev_node


if __name__ == "__main__":
    import doctest
    doctest.testmod()
