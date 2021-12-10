class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None

    def inorder(self,node,c):
        if node==None:
            return 1
        else:
            c=self.inorder(node.left,c)+self.inorder(node.right,c)
        return c

    def max_min(self,node,ma,mi):
        if node==None:
            return ma,mi
        else:
            if node.data>ma:
                ma=node.data
            if node.data<mi:
                mi=node.data
            ma,mi=self.max_min(node.left,ma,mi)
            ma,mi=self.max_min(node.right,ma,mi)
        return ma,mi

if __name__ == '__main__':
    ar=[]
    tre=tree()
    tre.root=node(1)
    tre.root.left=node(2)
    tre.root.right=node(3)
    tre.root.right.left=node(4)
    tre.root.right.right=node(6)
    tre.root.right.left.right=node(5)
    tre.root.right.left.right.left=node(7)

    # print(tre.inorder(tre.root,0))
    print(tre.max_min(tre.root,-99999999,999999999))

