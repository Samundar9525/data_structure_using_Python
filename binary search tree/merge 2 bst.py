class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None
        self.par = None

def inorder(node,arr):
    if node==None:
        return
    inorder(node.left,arr)
    arr.append(node.data)
    inorder(node.right,arr)


def insert(node,data):
    if node==None:
        return Node(data)
    # if node.data==data:
    #     return node

    if node.data>data:
        node.left=insert(node.left,data)
    elif node.data<data:
        node.right=insert(node.right,data)
    return node



def levelorder(node):
    if node==None:
        return
    que=[]
    que.append(node)
    que.append(None)
    while(que):
        t=que.pop(0)
        if t==None:
            print(" ")
            que.append(None)
            t=que.pop(0)
        if t!=None:
            print(t.data,end=" ")
            if t.left!=None:
                que.append(t.left)
            if t.right!=None:
                que.append(t.right)

def merge(node1,node2):
    arr=[]
    brr=[]
    inorder(node1,arr)
    inorder(node2,brr)
    print(arr)
    print(brr)
    res=[]
    i=0
    j=0
    while(i<len(arr) and j<len(brr)):
        if arr[i]<brr[j]:
            res.append(arr[i])
            i+=1
        elif arr[i]>brr[j]:
            res.append(brr[j])
            j+=1
        elif arr[i]==brr[j]:
            res.append(arr[i])
            res.append(brr[j])
            i+=1;j+=1
    while(i<len(arr)):
        res.append(arr[i])
        i=+1
    while(j<len(brr)):
        res.append(brr[j])
        j+=1
    print(res)




if __name__ == '__main__':
    arr=[8,9,6,7,10,12,3,5,7,2]
    brr=[4,13,3,1,18,100,200]
    tre1=tree()
    tre2=tree()
    tre1.root=Node(11)
    tre2.root=Node(16)
    for i in range(len(arr)):
        insert(tre1.root,arr[i])
    for i in range(len(brr)):
        insert(tre2.root,brr[i])
    merge(tre1.root,tre2.root)


