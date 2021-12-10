class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None



def top_view(node):
    que = []
    arr = {}
    res = {}
    que.append(node)
    arr[node] = 0

    while (len(que) != 0):
        t = que.pop(0)

        if arr[t] not in res:
            res[arr[t]] = [t]
        if t.left != None:
            que.append(t.left)
            arr[t.left] = arr[t] - 1
        if t.right != None:
            que.append(t.right)
            arr[t.right] = arr[t] + 1

    mi = 99999999
    ma = -9999999
    brr = []
    for i in res.keys():
        mi = min(mi, i)
        ma = max(ma, i)
    for i in range(mi, ma + 1):
        for j in res[i]:
            brr.append(j.data)
    print(brr)


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
    tre.root.right.left = node(6)
    tre.root.right.right = node(7)
    tre.root.right.right.left = node(9)
    tre.root.right.right.left.right = node(10)
    tre.root.left.left.left = node(8)

    top_view(tre.root)
    bottom_view(tre.root)