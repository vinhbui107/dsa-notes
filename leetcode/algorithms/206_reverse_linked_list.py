class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        curr_node = head

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        return prev_node


# a -> b -> c -> d -> null

# prev_node = null
# curr_node = a
# next_node = b

# first loop
# null <- a <- b
# prev_node.next = null
# prev_node = a
# curr_node = b
