class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None

def height_recursive(node):
    if node==None:
        return 0
    return(1+max(height_recursive(node.left),height_recursive(node.right)))

def diameter(node):             # sahi hai but tle de dega
    if node==None:
        return
    else:
        que=[]
        que.append(node)
        dia=-99999999999
        while(len(que)!=0):
            t=que.pop(0)

            if t.left!=None:
                que.append(t.left)
                lheight = height_recursive(t.left)
            if t.right!=None:
                que.append(t.right)
                rheight = height_recursive(t.right)
            dia=max(dia,lheight+rheight+1)
    return dia

arr=[-99999999]
def optimised_diameter(node,arr):
    if node==None:
        return 0
    left=optimised_diameter(node.left,arr)
    right=optimised_diameter(node.right,arr)

    arr[0]=max(arr[0],1+left+right)
    return(1+max(left,right))


if __name__ == '__main__':
    ar=[]
    tre=tree()
    tre.root=node(1)
    tre.root.left=node(2)
    tre.root.right=node(3)
    tre.root.right.left=node(4)
    tre.root.right.right=node(6)
    tre.root.right.right.right=node(8)
    tre.root.right.right.right.left=node(9)
    tre.root.right.left.right=node(5)
    tre.root.right.left.right.left=node(7)

    (optimised_diameter(tre.root,arr))
    print(arr[0])