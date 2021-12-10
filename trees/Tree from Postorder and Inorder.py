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

def tree(ino,post,st,inst,inen):
    if inst>inen:
        return None
    nod = Node(post[st[0]])
    st[0]-=1            #yahan refernce variable pass karna jaroori hai

    mid=search(ino,inst,inen,nod.data)
    nod.right = tree(ino, post, st, mid + 1, inen)
    nod.left=tree(ino,post,st,inst,mid-1)
    return nod

if __name__ == '__main__':
    ino=[4 ,8 ,2 ,5 ,1 ,6, 3 ,7]  # left-root-right
    post=[8 ,4 ,5 ,2 ,6 ,7, 3 ,1]  # root-left-right

    st=[len(ino)-1  ]
    root=tree(ino,post,st,0,len(ino)-1)
    preorder(root)