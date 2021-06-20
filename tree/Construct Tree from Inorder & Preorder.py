class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

def preorder(node):
    if node==None:
        return
    print(node.data,end=" ")
    preorder(node.left)
    preorder(node.right)

def search(arr,st,en,data):
    for i in range(st,en+1):
        if arr[i]==data:
            return i

def tree(ino,pre,st,inst,inen):
    if inst>inen:
        return None
    nod = Node(pre[st[0]])
    st[0]+=1            #yahan refernce variable pass karna jaroori hai
    # if inst==inen:
    #     return nod
    mid=search(ino,inst,inen,nod.data)
    nod.left=tree(ino,pre,st,inst,mid-1)
    nod.right=tree(ino,pre,st,mid+1,inen)
    return nod

if __name__ == '__main__':
    ino=[3 ,1 ,4 ,0 ,5 ,2]  # left-root-right
    pre=[0 ,1 ,3 ,4 ,2 ,5]  # root-left-right
    st=[0]
    root=tree(ino,pre,st,0,len(ino)-1)
    preorder(root)