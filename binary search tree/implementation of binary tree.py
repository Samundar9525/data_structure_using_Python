class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None
        self.par = None

def inorder(node):
    if node==None:
        return
    inorder(node.left)
    print(node.data,end=" ")
    inorder(node.right)


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

def find(node,key):
    if node==None:
        return node

    if node.data==key:
        return node

    if node.data<key:
        tre.par = node
        return find(node.right,key)
    if node.data>key:
        tre.par = node
        return find(node.left,key)


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



if __name__ == '__main__':
    arr=[8,9,6,7,10,12,3,5,7,2]
    tre=tree()
    tre.root=Node(11)
    for i in range(len(arr)):
        insert(tre.root,arr[i])
    inorder(tre.root)
    levelorder(tre.root)
    nod=(find(tre.root,10))

    print("adress of node :",nod)
    print(tre.par.data)

