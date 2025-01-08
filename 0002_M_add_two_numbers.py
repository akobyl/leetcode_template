"""
strategy:
- just like real life, we add digits starting at the 1's digit and work up
- we need to track the carry
- one number can be longer than the other
- the carry could be the only digit in the end, example: 5 + 6 = 11
- start with a dummy node so we can return that as the result
- loop through the digits, using 0 if one of lists is empty
- if at the end we have a carry, tack that on at the end
"""

from typing import Optional
from listnode.list_node import ListNode, create_node_list, list_to_string


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            value = val1 + val2 + carry
            current.next = ListNode(value % 10)
            carry = value // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next

        if carry:
            current.next = ListNode(carry)
        return dummy.next


s = Solution()


def test1():
    l1 = create_node_list([2, 4, 3])
    l2 = create_node_list([5, 6, 4])
    out = create_node_list([7, 0, 8])
    assert list_to_string(s.addTwoNumbers(l1, l2)) == list_to_string(out)


def test2():
    l1 = create_node_list([0])
    l2 = create_node_list([0])
    out = create_node_list([0])
    assert list_to_string(s.addTwoNumbers(l1, l2)) == list_to_string(out)


def test3():
    l1 = create_node_list([9, 9, 9])
    l2 = create_node_list([9])
    out = create_node_list([8, 0, 0, 1])
    assert list_to_string(s.addTwoNumbers(l1, l2)) == list_to_string(out)
