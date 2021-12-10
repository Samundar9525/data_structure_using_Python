class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None

def hei(node,csum,clen,masum,malen):
    if node==None:
        if malen[0]<clen:
            malen[0]=clen
            masum[0]=csum
        elif malen[0] < clen and csum>masum[0]:
            masum[0]=csum
        return 0
    l=hei(node.left,csum+node.data,clen+1,masum,malen)
    r=hei(node.right,csum+node.data,clen+1,masum,malen)


# def level(node):
#     que=[]
#     que.append(node)
#     que.append(None)
#     lev=0
#     ar={}
#
#     while(que):
#         t=que.pop(0)
#         if t==None:
#             print()
#             lev+=1
#             que.append(None)
#             t=que.pop(0)
#         if t!=None:
#             print(t.data,end=" ")
#             ar[t]=lev
#             if t.left!=None:
#                 que.append(t.left)
#             if t.right!=None:
#                 que.append(t.right)
#     return ar



def sol(node):
    arr={}
    masum = [-999999999999]
    malen = [0]
    (hei(node,0,0,masum,malen))
    print(masum)
    print(malen)







if __name__ == '__main__':
    tre=tree()
    tre.root=node(4)
    tre.root.left=node(2)
    tre.root.right=node(5)
    tre.root.left.left = node(8)
    tre.root.left.right = node(1)
    tre.root.right.left = node(2)
    tre.root.right.right = node(3)
    tre.root.left.right.left = node(6)
    sol(tre.root)




