class queue:
    def __init__(self,size):
        self.n = size
        self.que=[-1]*size
        self.top=-1
        self.rear=0

    def enqueue(self,x):

        if self.isfull(self.que):
            self.que[self.rear]=x
            self.display()
            self.rear =(self.rear+1)%self.n

        else:
            print("QUEUE IS FULL")


    def dequeue(self):
        if self.isempty():
            print("Queuue IS EMPTY")
        else:

            self.que[self.top]=-1
            self.display()
            self.top =(self.top+1)%self.n



    def isempty(self):
        if self.rear!=-1 or  self.top!=-1:
            return True
        else:
            return False



    def isfull(self,arr):
        return self.top!=(self.rear+1)%self.n


    def display(self):
        for i in self.que:
            print(i,end=" ")
        print("")



if __name__ == '__main__':
    ob=queue(5)
    ob.enqueue(10)
    ob.enqueue(20)
    ob.enqueue(30)
    ob.enqueue(40)
    ob.enqueue(50)
    ob.enqueue(60)
    ob.enqueue(60)
    ob.enqueue(60)
    ob.dequeue()
    ob.dequeue()
    ob.dequeue()
    ob.dequeue()
    ob.dequeue()
    ob.display()
    # ob.enqueue(60)
    # ob.dequeue()
    # ob.dequeue()
    # ob.enqueue(70)
    # ob.enqueue(80)
    # ob.enqueue(90)
    # # ob.dequeue()
