class nod:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None
def insert_recursively(root, key):
    if root!=None and  key==root.data:
        return root
    if root==None:
        t=nod(key)
        return t
    if root.data>key:
        root.left=insert_recursively(root.left,key)
    else:
        root.right=insert_recursively(root.right,key)
    return root


def push(node,stk,flag):
    if (flag==True):
        while(node!=None):
            stk.append(node)
            node=node.left
    else:
        while(node!=None):
            stk.append(node)
            node=node.right
def solution(node,target):
    res=[]
    if node==None:
        return
    stk1=[]
    stk2=[]
    push(node,stk1,True)
    push(node,stk2,False)

    while(len(stk1)!=0 and len(stk2)!=0 and stk1[-1].data<=stk2[-1].data):
        x=stk1[-1]
        y=stk2[-1]
        if x.data+y.data == target and x!=y:
            print(x.data,y.data)
            # res.append((x.data,y.data))          #agar pair chaiiye toh uncomenyt karke return true hata do
            return True
        if x.data+y.data<target:
            temp=stk1[-1]
            stk1.pop()
            push(temp.right,stk1,True)
        else:
            temp=stk2[-1]
            stk2.pop()
            push(temp.left,stk2,False)
    # return res
    return False





def inord(node, arr):
    if node == None:
        return
    inord(node.left, arr)
    arr.append(node.data)
    inord(node.right, arr)


def sol(root, arr,target):

    st = 0
    en = len(arr) - 1
    while (st < en):
        if arr[st] + arr[en] == target:
            return 1
        if arr[st] + arr[en] >= target:
            en -= 1
        elif arr[st] + arr[en] < target:
            st += 1
    return 0





def inorder(node):
    if node==None:
        return
    inorder(node.left)
    print(node.data,end=" ")
    inorder(node.right)


if __name__ == '__main__':
    tre=tree()
    arr=[12,8,5,9,11,7,16]
    tre.root=nod(10)
    for i in arr:
        insert_recursively(tre.root,i)

    inorder(tre.root)
    print()
    print(solution(tre.root,24))
    print()
    arr = []
    inord(tre.root,arr)
    print(sol(tre.root,arr,24))


