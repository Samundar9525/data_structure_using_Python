class queue:

    def __init__(self,size):
        self.que=[]
        self.n=size

    def enqueue(self,data):
        if self.isfull():
            print("QUEUE is full")
        else:
            self.que.append(data)

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
        else:
            return self.que.pop(0)

    def isfull(self):
        if len(self.que)>=self.n:
            return True
        else:
            return False
    def isempty(self):
        if len(self.que)<1:
            return True
        else:
            return False
    def display(self):
        for i in range(len(self.que)):
            print(self.que[i] ,end=" ")
        print(" ")


    def sol(self):
        mid=self.n//2
        que1=[]
        que2=[]
        for i in range(len(self.que)):
            if i%2==0:
                que1.append(self.dequeue())
            else:
                que2.append(self.dequeue())
        res=[]
        print(que1,que2)
        for i in range(mid):
            res.append(que1.pop(0))
            # res.append(que2.pop(0))
        print(res)







if __name__ == '__main__':
    ob=queue(10)
    ob.enqueue(11)
    ob.enqueue(12)
    ob.enqueue(13)
    ob.enqueue(14)
    ob.enqueue(15)
    ob.enqueue(16)
    ob.enqueue(17)
    ob.enqueue(18)
    ob.enqueue(19)
    ob.enqueue(20)
    ob.display()
    ob.sol()



