class sol:
    def __init__(self):
        self.stk1=[]

    def enqueue(self,x,arr):
        arr.append(x)
    def dequeue(self,arr):
        return arr.pop(0)

    def push(self,x):
        self.enqueue(x,self.stk1)

    def pop(self):
        self.stk1=self.stk1[::-1]
        temp= self.dequeue(self.stk1)
        self.stk1 = self.stk1[::-1]
        return temp

if __name__ == '__main__':
    ob=sol()
    ob.push(10)
    ob.push(20)
    ob.push(30)
    print(ob.pop())
    print(ob.pop())
    ob.push(40)
    ob.push(50)
    ob.push(60)
    print(ob.pop())
    print(ob.pop())


