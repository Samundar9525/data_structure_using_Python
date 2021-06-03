class node:
    def __init__(self,dat):
        self.data=dat
        self.next=None

def display(head):
    p=head
    while(p!=None):
        print(p.data,end=' ')
        p=p.next


def detectLoop( head):
    # code here
    p = head
    t = p
    h = p
    while (h!=None and t!=None and h.next!=None ):
        t = t.next
        h = h.next.next
        if t ==h:
            print("loop ba")
            return True
    print("NA ba")



def detect_by_hash(head):
    dic={}
    p=head

    while (p!=None):
        if p not in dic:
            dic[p]=1
        else:
            print("LOOP BA isme ")
            return True
        p=p.next
    print("NO no no no no ")




if __name__ == '__main__':
    head=None
    head=node(1)
    head.next=node(2)
    head.next.next=node(3)
    head.next.next.next=node(4)
    head.next.next.next.next=node(5)
    head.next.next.next=head.next



    detectLoop(head)
    # display(head)

    detect_by_hash(head)