class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None



def diagonal(node):
    que=[]
    dic={}
    res={}
    que.append(node)
    dic[node]=0

    while(que):
        t=que.pop(0)
        if dic[t] not in res:
            res[dic[t]]=[t]
        else:
            temp=res[dic[t]]
            temp.append(t)
            res[dic[t]] = temp
        if t.left!=None:
            que.append(t.left)
            dic[t.left]=dic[t]+1
        if t.right!=None:
            que.append(t.right)
            dic[t.right] = dic[t]

    mi=min(res.keys())
    ma=max(res.keys())
    brr=[]
    for i in range(mi,ma+1):
        for j in res[i]:
            brr.append(j.data)
    print(brr)


def diagonal2(node):
    que=[]
    que.append(node)
    res=[]
    while(len(que)!=0):
        t=que.pop(0)
        while(t!=None):
            if t!=None:
                res.append(t.data)
                if t.left!=None:
                    que.append(t.left)
            t = t.right
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

    diagonal(tre.root)
    diagonal2(tre.root)