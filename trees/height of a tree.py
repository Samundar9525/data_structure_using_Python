class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None

    def height(self,node):
        # print(node.data)
        que=[]
        que.append(node)
        que.append(None)
        c=0
        while(len(que)!=0):
            t=que.pop(0)
            if t==None:
                c+=1
                que.append(None)
                t=que.pop(0)
            if t!=None:
                if t.left!=None:
                    que.append(t.left)
                if t.right!=None:
                    que.append(t.right)
        return c


def height_recursive(node):
    if node==None:
        return 0
    return(1+max(height_recursive(node.left),height_recursive(node.right)))


if __name__ == '__main__':
    ar=[]
    tre=tree()
    tre.root=node(1)
    tre.root.left=node(2)
    tre.root.right=node(3)
    tre.root.right.left=node(4)
    tre.root.right.right=node(6)
    tre.root.right.left.right=node(5)
    tre.root.right.left.right.left=node(7)

    print("height_iteratevely : ",tre.height(tre.root))
    print("height_recursively : ",height_recursive(tre.root))