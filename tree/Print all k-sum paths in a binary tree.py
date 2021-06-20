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


def all_path(node,arr,indx,fin):
    if node==None:
        return
    arr[indx] = node.data
    if node.left == None and node.right == None:
        res=[]
        # for i in range (indx+1):
        #     res.append(arr[i])
        fin.append(arr[0:indx+1])
        return
    all_path(node.left,arr,indx+1,fin)
    all_path(node.right,arr,indx+1,fin)









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
    arr=[0]*10
    all_path(tre.root,arr,0,fin)
    print(fin)