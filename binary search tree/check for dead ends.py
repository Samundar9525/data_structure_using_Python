# Your task is to complete this function
# function should return true/false or 1/0
def isdeadEnd(root):
    # Code here
    res = [0]

    def sol(node, low, high, res):
        if node == None:
            return
        # print(node.data,low,high)
        if node.left == None and node.right == None:
            if low == high:
                # print("hello")
                res[0] = 1

        sol(node.left, low, node.data - 1, res)
        sol(node.right, node.data + 1, high, res)

    low = 1
    high = 9999999999
    sol(root, low, high, res)
    return res[0]


# {
#  Driver Code Starts
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        elif root.data == node.data:
            return
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def traverseInorder(root):
    if root is not None:
        traverseInorder(root.left)
        print(root.data, end=" ")
        traverseInorder(root.right)


if __name__ == '__main__':

    arr=[8 ,5 ,9 ,7 ,2, 1]
    root = None
    for j in arr:
        if root is None:
            root = Node(j)
        else:
            insert(root, Node(j))
    if isdeadEnd(root):
        print("DEAD END BA ")
    else:
        print("NO DEAD END BA")
