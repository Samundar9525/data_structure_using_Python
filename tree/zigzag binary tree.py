class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None



def zigzag(node):
    # YAHAN 2 STACK KA USE HOGA
    stk1=[]
    stk2=[]
    stk1.append(node)
    res=[]
    while(len(stk1)!=0 or len(stk2)!=0 ):
        while(len(stk1)!=0):
            t=stk1.pop()
            res.append(t.data)
            if t.left!=None:
                stk2.append(t.left)
            if t.right!=None:
                stk2.append(t.right)

        while(len(stk2)!=0):
            p=stk2.pop()
            res.append(p.data)
            if p.right!=None:
                stk1.append(p.right)
            if p.left!=None:
                stk1.append(p.left)
    print(res)







if __name__ == '__main__':
    ar=[]
    tre=tree()
    tre.root = node(1)
    tre.root.left = node(2)
    tre.root.right = node(3)
    tre.root.left.left = node(4)
    tre.root.left.right = node(5)
    tre.root.right.left = node(6)
    tre.root.right.right = node(7)

    zigzag(tre.root)