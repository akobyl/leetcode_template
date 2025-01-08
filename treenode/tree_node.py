import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return f"({self.val}) | {self.left} - {self.right}"


def build_tree(nodes: list) -> TreeNode | None:
    n = len(nodes)

    if n == 0:
        return None

    parentStack = collections.deque()
    root = TreeNode(nodes[0])
    curParent = root

    for i in range(1, n):
        if i % 2 == 1:
            if nodes[i] is not None:
                curParent.left = TreeNode(nodes[i])
                parentStack.append(curParent.left)
        else:
            if nodes[i] is not None:
                curParent.right = TreeNode(nodes[i])
                parentStack.append(curParent.right)

            curParent = parentStack.popleft()

    return root


def print_tree(root):
    if root is None:
        return

    height = get_height(root)
    width = 2**height - 1

    tree_array = [[" " for _ in range(width)] for _ in range(height)]
    fill_tree_array(tree_array, root, 0, 0, width - 1)

    for row in tree_array:
        print("".join(row))


def fill_tree_array(tree_array, node, level, left, right):
    if node is None:
        return

    mid = (left + right) // 2
    tree_array[level][mid] = str(node.val)

    fill_tree_array(tree_array, node.left, level + 1, left, mid - 1)
    fill_tree_array(tree_array, node.right, level + 1, mid + 1, right)


def get_height(node):
    if node is None:
        return 0
    return 1 + max(get_height(node.left), get_height(node.right))


if __name__ == "__main__":
    x = build_tree([1, None, 2, 3])
    print_tree(x)

    y = build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])
    print_tree(y)
