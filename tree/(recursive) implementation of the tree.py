class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class tree:

    def __init__(self):
        self.root=None
        self.p=None

    def insert(self,data,nod):
        if self.root==None:
            self.root=node(data)
            return self.root
        else:
            if nod==None:
                nod=node(data)
            self.insert(data,nod.left)
            self.insert(data,nod.right)







def levelorder(root):
    que=[]
    que.append(root)
    que.append(None)
    while(len(que)!=0):
        t=que.pop()
        if t==None:
            print("")
            que.append(None)
            t = que.pop(0)
        if t!=None:
            print(t.data,end=" ")
            if t.left!=None:
                que.append(t.left)
            if t.right!=None:
                que.append(t.right)






if __name__ == '__main__':
    arr=[7,11,10,15,9,8,6,16,5]
    tre=tree()
    root=tre.insert(arr[0],None)
    arr.pop(0)
    # for i in arr:
    #     root=tre.insert(i,root)
    levelorder(root)

