class node:
    def __init__(self,d):
        self.data=d
        self.next=None

class graph:
    def __init__(self,vertex):
        self.v=vertex
        self.arr=[None]* self.v

    def add(self,src,dest):
        nod=node(dest)
        nod.next=self.arr[src]
        self.arr[src]=nod
        # syymetriccity banana hai to uske liye ye hai
        nod1=node(src)
        nod1.next=self.arr[dest]
        self.arr[dest]=nod1
        #--------------------aur is tarah undirected graph bananae ka process poora hua ----------

    def cycle(self):
        visited= [-1] * self.v
        queue=[]
        l=self.arr[0]
        queue.append(l.data)
        visited[l.data]+=1
        while(queue):
            temp=queue.pop(0)
            if (visited[temp]==0):
                #print(temp, end=" ")
                visited[temp] += 1
                ptr=self.arr[temp]
                while(ptr!=None):
                    queue.append(ptr.data)
                    if (visited[ptr.data] == 0):
                        print("Cycle detected")
                        return 0
                    else:
                        visited[ptr.data]+=1
                    ptr=ptr.next



if __name__ == '__main__':
    g=graph(5)
    g.add(0,2)
    #g.add(0,1)
    g.add(1,2)
    g.add(2,3)
    g.add(3,4)
    #g.add(4,2)
    if(g.cycle()==0):
        pass
    else:
        print("Not ANY cycle")



