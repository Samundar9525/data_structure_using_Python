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




def decreasing_order(node):
    stk=[]
    stk.append(node)
    t=node
    while(len(stk)!=0):
        if (t!=None):
            stk.append(t)
            t=t.right
        elif t==None:
            t=stk.pop(-1)
            if len(stk)!=0:
                print(t.data,end=" ")
            t=t.left


def increasing_order(node):
    stk=[]
    stk.append(node)
    t=node
    while(len(stk)!=0):
        if (t!=None):
            stk.append(t)
            t=t.left
        elif t==None:
            t=stk.pop(-1)
            if len(stk)!=0:
                print(t.data,end=" ")
            t=t.right

def inorder(node):
    if node==None:
        return
    inorder(node.left)
    print(node.data,end=" ")
    inorder(node.right)





if __name__ == '__main__':
    tre=tree()
    arr=[12,8,5,9,12,11,7,16]
    tre.root=nod(10)
    for i in arr:
        insert_recursively(tre.root,i)

    inorder(tre.root)
    print("\nincreasing order : ",end=" ")
    increasing_order(tre.root)
    print("\ndecreasing order : ",end=" ")
    decreasing_order(tre.root)
    print()


