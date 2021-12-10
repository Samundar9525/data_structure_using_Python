class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None


def level_order_view(node):
    que=[]
    temp=[]
    res=[]
    que.append(node)
    que.append(None)
    while(len(que)!=0):
        t=que.pop(0)
        if t==None:
            if len(temp)!=None:
                res.append(temp[-1])
                temp=[]
            que.append(None)
            t=que.pop(0)
        if t!=None:
            temp.append(t.data)
            if t.left!=None:
                que.append(t.left)
            if t.right!=None:
                que.append(t.right)
    return res





if __name__ == '__main__':
    ar=[]
    tre=tree()
    tre.root=node(1)
    tre.root.left=node(2)
    tre.root.right=node(3)
    tre.root.left.left=node(4)
    tre.root.left.right=node(5)
    tre.root.right.left=node(6)
    tre.root.right.right=node(7)
    tre.root.left.left.right = node(8)

    print(level_order_view(tre.root))