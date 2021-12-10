class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Graph:
    def __init__(self,vertex):
        self.v=vertex
        self.graph=[None]*vertex
        print(self.graph)


    def add_edge(self,dest,src):
        nod=node(dest)
        nod.next=self.graph[src]
        self.graph[src]=nod

        nod=node(src)
        nod.next=self.graph[dest]
        self.graph[dest]=nod

    def display(self):
        for i in range(self.v):
            if self.graph[i] !=None:
                temp=self.graph[i]
                print("head",i,end="")
                while(temp):
                    print(" --> %d"%temp.data,end=" ")
                    temp=temp.next
                print()

if __name__ == '__main__':
    graph=Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    print(graph.graph)
    graph.display()