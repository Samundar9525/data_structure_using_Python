class node:
    def __init__(self,d):
        self.data=d
        self.next=None
class graph:
    def __init__(self,ver):
        self.v=ver
        self.arr = [None] * self.v

    def add(self,src,dest):
        nod=node(dest)
        nod.next=self.arr[src]
        self.arr[src]=nod

        nod1=node(src)
        nod1.next=self.arr[dest]
        self.arr[dest]=nod1

    def iscycle(self):
        visited=[-1]*self.v
        stk=[]
        stk.append(0)
        parent=node(-1)
        parent_table=[None]*self.v
        parent_table[0]=-1
        while(stk):
            temp=stk.pop()
            #print(temp,end=" ")
            visited[temp]=1
            t=self.arr[temp]

            while(t!=None):
                parent = t
                if (visited[t.data]==-1):
                    stk.append(t.data)
                    visited[t.data]+=1

                elif (visited[t.data]==0):
                    if (parent.data==parent_table[t.data]):
                        # print("-->",parent.data ,parent_table[t.data])
                       return True
                parent_table[t.data]=parent.data
                t=t.next

if __name__ == '__main__':
    g=graph(6)
    g.add(0,1)
    g.add(0,5)
    g.add(1,2)
    g.add(2,3)
    g.add(3,4)
    g.add(4,5)

    # g.add(1,2)
    # g.add(2,3)
    # #g.add(4,2)
    # g.add(3,4)
    # g.add(4,5)
    # g.add(2,5)            # sara logic sahi hai but permuation lagaya hai code me par ye kam kar raha hai kaise ???
                           # isko pata karo kyunki notes me likhna hai taki yaad rahe sam.....
    if (g.iscycle()):
        print("Cycle Detected")
    else:
        print("Cycle NOT Detected")