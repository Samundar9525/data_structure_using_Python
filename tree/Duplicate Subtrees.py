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


def duplicate(node,arr):
    if node==None:
        return "X"

    print(node.data)
    l=duplicate(node.left,arr)
    r=duplicate(node.right,arr)

    p=str(node.data)+l+r
    if p not in arr:
        arr[p]=1
    else:
        arr[p]+=1
    return p





if __name__ == '__main__':
    arr={}
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
    # level_order_view(tre.root)
    duplicate(tre.root,arr)
    print(arr)
