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
                print("")
                res.append(temp[-1])
                temp=[]
            que.append(None)
            t=que.pop(0)
        if t!=None:
            print(t.data,end=" ")
            temp.append(t.data)
            if t.left!=None:
                que.append(t.left)
            if t.right!=None:
                que.append(t.right)


def lca(node,a,b):
    if node==None:
        return
    if node.data==a or node.data==b:
        return node

    l=lca(node.left,a,b)
    r=lca(node.right,a,b)

    if l!=None and r!=None:
        return node
    if l!=None:
        return l
    if r!=None:
        return r











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
    fin=[]
    level_order_view(tre.root)
    a=5
    b=8
    print(lca(tre.root,a,b).data)
