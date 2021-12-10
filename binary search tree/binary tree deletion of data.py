class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None
        self.par = None

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

def delete(node,key):
    if node==None:
        return node

    if node.data>key:
        node.left= delete(node.left,key)
        return node
    if node.data<key:
        node.right= delete(node.right,key)
        return node
#=====================================================================================
    if node.data==key:
        if node.left==None and node.right==None:
            return None

        if node.right!=None and node.left==None:
            tem=node.right
            node=None
            return tem
        if node.left!=None and node.right==None:
            tem=node.left
            node=None
            return tem

        if node.left!=None and node.right!=None:
            par=node
            p=node.right

            while(p.left!=None):
                par=p
                p=p.left
            if par!= node:
                par.left =p.right
            else:
                par.right = p.right

            node.data=p.data
            return node







if __name__ == '__main__':
    arr=[8,9,6,7,10,12,3,5,7,2]
    # arr=[]
    tre=tree()
    tre.root=Node(15)
    for i in range(len(arr)):
        insert(tre.root,arr[i])
    levelorder(tre.root)

    tre.root=(delete(tre.root,6))
    print("jkjk")
    levelorder(tre.root)



