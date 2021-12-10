class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None



def bottom_view(node):
    que=[]
    que.append(node)
    dic={}
    res={}
    dic[node]=0
    while(len(que)!=0):
        t=que.pop(0)
        res[dic[t]]=t
        if t.left!=None:
            que.append(t.left)
            dic[t.left]=dic[t] - 1
        if t.right !=None:
            que.append(t.right)
            dic[t.right] = dic[t] + 1

    mi=min(res.keys())
    ma=max(res.keys())
    brr=[]
    for i in range(mi,ma+1):
        brr.append(res[i].data)
    print(brr)









if __name__ == '__main__':
    ar=[]
    tre=tree()
    tre.root=node(1)
    tre.root.left=node(2)
    tre.root.right=node(3)
    tre.root.left.left = node(4)
    tre.root.left.right = node(5)
    tre.root.left.right.right = node(8)
    tre.root.left.right.right.left = node(9)
    tre.root.left.right.right.right = node(10)

    tre.root.right.left = node(6)
    tre.root.right.right = node(7)


    # tre.root.right.right.left = node(9)
    # tre.root.right.right.left.right = node(10)
    # tre.root.left.left.left = node(8)

    bottom_view(tre.root)