class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def level(node):
    que=[]
    que.append(node)
    que.append(None)
    lev=0
    ar={}

    while(que):
        t=que.pop(0)
        if t==None:
            print()
            lev+=1
            que.append(None)
            t=que.pop(0)
        if t!=None:
            print(t.data,end=" ")
            ar[t]=lev
            if t.left!=None:
                que.append(t.left)
            if t.right!=None:
                que.append(t.right)
    return ar


class tree:
    def __init__(self):
        self.root=None


def sol(node,ma):
    if node==None:
        return 0
    l=sol(node.left,ma)
    r=sol(node.right,ma)
    p= l+r+node.data
    ma[0]=max(ma[0],p)
    return p


if __name__ == '__main__':
    tre=tree()
    tre.root=node(1)
    tre.root.left=node(-2)
    tre.root.right=node(3)
    tre.root.left.left = node(4)
    tre.root.left.right = node(5)
    tre.root.right.left = node(-6)
    tre.root.right.right = node(2)
    # tre.root.left.right.left = node(6)
    ma=[-999999999]
    level(tre.root)
    sol(tre.root,ma)
    print("\n----------MAX SUM : %d ----------------"%ma[0])
    level(tre.root)



