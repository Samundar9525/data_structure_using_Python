class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


class tree:
    def __init__(self):
        self.root=None
        self.que=[]

    def insert(self,data):
       if self.root==None:
           self.root=node(data)
           self.que.append(self.root)
       else:
           p=self.que[0]
           if p.left!=None and p.right!=None:
               self.que.pop(0)
           elif p.left==None:
               p.left=node(data)
               self.que.append(p.left)
           elif p.right==None:
               p.right = node(data)
               self.que.append(p.right)
           if p.left!=None and p.right!=None:
               self.que.pop(0)
       return self.root




def levelorder(root):
    p=None # for tracking last node
    que=[]
    arr=[]
    que.append(root)
    que.append(None)
    while(len(que)!=0):
        t=que.pop(0)
        if t==None:
            print(" ")
            que.append(None)
            t=que.pop(0)
        if t!=None:
            p=t
            arr.append(t.data)
            if t.left != None:
                que.append(t.left)
            if t.right != None:
                que.append(t.right)
    return arr




if __name__ == '__main__':
    arr=[1 ,4, 1,7 ,5, 6,1 ]
    tr=tree()
    root=None
    for i in range(len(arr)):
        root=tr.insert(arr[i])
    print(levelorder(tr.root))
