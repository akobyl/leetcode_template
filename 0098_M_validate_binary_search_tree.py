"""
strategy:
- a BST is a tree where all the values are in order
- the value >= left node (if it exists) and <= right node (if it exists)
- we can then check the left node and right node, passing in the min/max values from the current node
"""

from typing import Optional
from treenode.tree_node import TreeNode, build_tree, print_tree


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid_bst(node, min_val, max_val):
            if node is None:
                return True

            if node.val <= min_val or node.val >= max_val:
                return False

            return valid_bst(node.left, min_val, node.val) and valid_bst(
                node.right, node.val, max_val
            )

        return valid_bst(root, float("-inf"), float("inf"))


def test1():
    s = Solution()
    input = build_tree([2, 1, 3])
    print_tree(input)
    assert s.isValidBST(input)


def test2():
    s = Solution()
    input = build_tree([5, 1, 4, None, None, 3, 6])
    print_tree(input)
    assert not s.isValidBST(input)
