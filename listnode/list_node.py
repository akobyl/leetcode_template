from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        next_str = self.next.val if self.next else None
        return f"{self.val} -> {next_str}"

    def __repr__(self):
        return self.__str__()


def create_node_list(nodes: List[int]):
    if not nodes:
        return None

    head = ListNode(nodes[0])
    current = head

    for val in nodes[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def print_node_list(node: Optional[ListNode]):
    current = node
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


def list_to_string(node: Optional[ListNode]) -> str:
    current = node
    result = ""
    while current:
        result += f"{current.val} "
        current = current.next
    return result.rstrip()
