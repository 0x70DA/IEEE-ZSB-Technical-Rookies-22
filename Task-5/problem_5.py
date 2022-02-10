'''HackerRank: Binary Search Tree : Insertion'''


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        # If the tree is empty, add the new node as root.
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            return
        # Traverse the tree to find the correct spot.
        current_node = self.root
        while current_node is not None:
            if new_node.info < current_node.info:
                if current_node.left is None:
                    current_node.left = new_node
                    return
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return
                else:
                    current_node = current_node.right


if __name__ == '__main__':
    tree = BinarySearchTree()
    t = int(input())

    arr = list(map(int, input().split()))

    for i in range(t):
        tree.insert(arr[i])

    preOrder(tree.root)
