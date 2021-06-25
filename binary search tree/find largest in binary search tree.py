class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
def inorder(node):
    if node==None:
        return
    inorder(node.left)
    print(node.data,end=" ")
    inorder(node.right)

class tree:
    def __init__(self):
        self.root=None


class bst:
    def __init__(self,flag,size,ma,mi):
        self.isbst=flag
        self.size=size
        self.maxele=ma
        self.minele=mi

def sol(node):
    if node==None:
        return(bst(True,0,-9999999,99999999))
    l=sol(node.left)
    r=sol(node.right)

    if l.isbst==True and r.isbst==True and l.maxele<node.data and r.minele>node.data  :
        b=bst(True,1+l.size+r.size,min(node.data,l.minele),max(node.data,r.maxele))
        return b
    else:
        b = bst(False, max( l.size , r.size), -1,-1)
        return b



if __name__ == '__main__':
    tre=tree()
    tre.root=Node(6)
    tre.root.left=Node(6)
    tre.root.right=Node(3)
    tre.root.left.right=Node(2)
    tre.root.left.right.right=Node(8)
    tre.root.right.right=Node(3)
    tre.root.right.left=Node(9)
    tre.root.right.left.left=Node(8)
    tre.root.right.left.right=Node(2)
    inorder(tre.root)
    res=sol(tre.root)
    print()
    print(res.size)
    print("hello")