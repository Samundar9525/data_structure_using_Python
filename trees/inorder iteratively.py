class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None

def inorder(node):
    if node==None:
        return
    else:
        inorder(node.left)
        print(node.data,end=" ")
        inorder(node.right)

def inorder_iteratively(node):
    stk=[]
    stk.append(node)
    curr=node

    while(len(stk)!=0 ):

        if curr!=None:
            stk.append(curr)
            curr=curr.left
        else:
            curr=stk.pop()
            if len(stk)>=1:
                print(curr.data,end=" ")
            curr=curr.right



if __name__ == '__main__':
    ar=[]
    tre=tree()
    tre.root=node(1)
    tre.root.left=node(2)
    tre.root.right=node(3)
    tre.root.left.left=node(4)
    tre.root.left.right=node(5)
    tre.root.right.right=node(6)
    tre.root.left.left.left = node(9)
    tre.root.left.left.right = node(10)

    (inorder(tre.root))
    print()
    inorder_iteratively(tre.root)