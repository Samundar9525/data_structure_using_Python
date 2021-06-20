class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None

def lb(node):
    if node==None:
        return
    arr = []
    while(node!=None):
        if node.left==None and node.right==None:
            break
        arr.append(node.data)
        if node.left!=None:
            node=node.left
        elif node.right!=None:
            node=node.right
    return(arr)

def rb(node):
    if node==None:
        return
    arr = []
    while(node!=None):
        if node.left==None and node.right==None:
            break
        arr.append(node.data)
        if node.right!=None:
            node=node.right
        elif node.left!=None:
            node=node.left
    return(arr[::-1])

def leaf(node,arr):
    if node==None:
        return
    leaf(node.left,arr)
    if node.left==None and node.right==None:
        arr.append(node.data)
    leaf(node.right,arr)


def boundary(node):
    l=(lb(node.left))
    r=(rb(node.right))
    lf=[]
    leaf(node,lf)
    print(lf)
    res=l+lf+r+[node.data]
    print(res)


if __name__ == '__main__':
    ar=[]
    tre=tree()
    tre.root=node(1)
    tre.root.left=node(2)
    tre.root.right=node(3)
    tre.root.left.left = node(4)
    tre.root.left.right = node(5)
    tre.root.left.right.left = node(8)
    tre.root.left.right.right = node(9)
    tre.root.right.left = node(6)
    tre.root.right.right = node(7)
    tre.root.right.right.left = node(10)

    # tre.root.right.left=node(4)
    # tre.root.right.right=node(6)
    # tre.root.right.left.right=node(5)
    # tre.root.right.left.right.left=node(7)

    boundary(tre.root)


