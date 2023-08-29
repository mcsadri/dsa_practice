# in class review: https://replit.com/@adamOwada/Binary-Tree-Review#main.py
# CF documentation: https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-15/resources/Trees.html
# geeksforgeeks reference: https://www.geeksforgeeks.org/level-order-tree-traversal/
# binary tree class only knows about the root
# binary tree node class knows about its value, and left and right pointers
# binary search trees must be ordered
# look up accumulator pattern

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# breadth first search traversal and print of a binary tree
def bfs_print_tree(bt):
    q = [bt]

    while q:
        # dequeue
        node = q.pop(0)

        # do a thing
        print(node.value)

        # conditionally enqueue node's children
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


# recursive in-order depth-first traversal
def in_order_dfs_print_tree(bt):

    # helper function
    def walk(root):
        if root is None:
            return
        # do operations
        walk(root.left)  # traverse left
        print(root.value)  # perform logic with the root node
        walk(root.right)  # traverse right

    # invoke the helper function
    walk(bt)


# class BT:
#     def __init__(self, root=None):
#         self.root = root


if __name__ == "__main__":
    """
    #     1
    #    / \
    #   2   3
    #  /\   /\
    # 4  5 6  7
    """
    bt_1 = Node(1)
    bt_1.left = Node(2)
    bt_1.right = Node(3)
    bt_1.left.left = Node(4)
    bt_1.left.right = Node(5)
    bt_1.right.left = Node(6)
    bt_1.right.right = Node(7)

    # bfs_print_tree(bt_1)
    in_order_dfs_print_tree(bt_1)
