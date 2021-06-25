class nod:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None

    def insert_iteratively(self,key):
        if self.root==None:
            self.root=nod(key)
        p=self.root
        while(p!=None):
            if key==p.data:
                return
            if key>p.data:
                if p.right==None:
                    t=nod(key)
                    p.right=t
                    break
                p=p.right
            else:
                if p.left==None:
                    t=nod(key)
                    p.left=t
                    break
                p=p.left
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
    tre.insert_iteratively(6)
    inorder(tre.root)


