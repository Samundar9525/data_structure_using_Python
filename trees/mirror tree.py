class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None


def level_order_view(node):
    que=[]
    que.append(node)
    que.append(None)
    while(len(que)!=0):
        t=que.pop(0)
        if t==None:
            print("")
            que.append(None)
            t=que.pop(0)
        if t!=None:
            print(t.data ,end=" ")
            if t.left!=None:
                que.append(t.left)
            if t.right!=None:
                que.append(t.right)

def mirror(node):
    if node==None:
        return 0
    mirror(node.left)
    mirror(node.right)
    node.left,node.right=node.right,node.left



if __name__ == '__main__':
    ar=[]
    tre=tree()
    tre.root=node(1)
    tre.root.left=node(2)
    tre.root.right=node(3)
    tre.root.left.left = node(4)
    tre.root.left.right = node(5)
    tre.root.right.left = node(6)
    tre.root.right.right = node(7)

    # tre.root.right.left=node(4)
    # tre.root.right.right=node(6)
    # tre.root.right.left.right=node(5)
    # tre.root.right.left.right.left=node(7)

    level_order_view(tre.root)
    mirror(tre.root)
    print("After mirroring")
    level_order_view(tre.root)


