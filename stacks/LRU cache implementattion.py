class node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None
class lru:
    def __init__(self,cap):
        self.head=None
        self.tail=None
        self.di={}
        self.n=cap


    def get(self,key):
        if key in self.di.keys():
            return self.di[key].data
        else:
            return -1


    def set(self,key,value):
        def insert_end(data):
            if self.head==None and self.tail==None:
                p=node(data)
                self.head=p
                self.tail=p
                return self.tail
            else:
                p=self.tail
                q=node(data)
                p.next = q
                q.prev=p
                self.tail=q
                return self.tail

        def delete_top():
            p=self.head
            q=p.next
            self.head=q
            return p

        loc=insert_end(value)

        if value not in self.di.values() and len(self.di)<self.n :
            self.di[key]=loc
        if len(self.di)>=self.n:
            te=delete_top()
            # print(te.data)
            # print(self.di)
            # val = list(self.di.values())
            # self.di.pop(val.index(te) + 1)



if __name__ == '__main__':
    ob=lru(3)
    ob.set(1,2)
    ob.set(2,3)
    ob.set(1,5)
    ob.set(4,5)
    ob.set(6,7)
    print(ob.get(4))
    ob.set(1,2)
    print(ob.get(3))
