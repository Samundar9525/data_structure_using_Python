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




    def delete(self,data):
        que=[]
        que.append(self.root)
        while(len(que)!=0):
            p = que[0]
            if data==p.data:
                te=levelorder(self.root)
                te.data,p.data=p.data,te.data
                te.data=None
                return
            else:
                if p.left!=None:
                    que.append(p.left)
                if p.right!=None:
                    que.append(p.right)
                que.pop(0)
        print("Data not found")             # isese data swap toh ho ja raha hai but delete nahi
                                            # brute force mai ya  toh phir se traverse kar doon ya koi stack sab ka use kar loon bv
def levelorder(root):
    p=None # for tracking last node
    que=[]
    que.append(root)
    que.append(None)
    while(len(que)!=0):
        t=que.pop(0)
        if t==None:
            # print(" ")
            que.append(None)
            t=que.pop(0)
        if t!=None:
            p=t         #isse last element fetch ho ja raha hai
            # print(t.data,end=" ")
            if t.left != None:
                que.append(t.left)
            if t.right != None:
                que.append(t.right)
    return p

def inorder(temp):
    if (not temp):
        return
    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)

def delhelper(temp):
    if (not temp):
        return
    if temp.right!=None and temp.left!=None:
        if temp.right.data==None or temp.left.data==None:
            if temp.right.data==None:
                temp.right=None
            else:
                temp.left=None
    delhelper(temp.left)
    delhelper(temp.right)


if __name__ == '__main__':
    arr=[1 ,4, 1,7 ,5, 6,1 ]
    tr=tree()
    root=None
    for i in range(len(arr)):
        root=tr.insert(arr[i])
    inorder(tr.root)
    print("")
    n=int(input("Enter data to be deteted : "))
    tr.delete(n)
    print("After data detetion\n")
    delhelper(tr.root)
    inorder(tr.root)
