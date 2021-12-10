class Node:
    def __init__(self):
        self.data = None
        self.prev = None
        self.next = None


def findlast(head):
    while(head.next!=None):
        head=head.next
    return head


def countTriplets(head, x):
   p=head
   ans=[]
   while(p!=None):
       st=p.next
       end = findlast(head)
       while(st!=None and end!=None and st.data<end.data):
           # print(st.data,end.data)
           if p.data+st.data+end.data==x:
               ans.append((p.data,st.data,end.data))
               st=st.next
           elif p.data+st.data+end.data<x:
               st=st.next
           else:
               end=end.prev
       p=p.next
   return ans

def display(head):
    while(head!=None):
        print(head.data,end=" ")
        head=head.next
    print()

def insert(head, data):
    temp = Node()
    temp.data = data
    temp.next = temp.prev = None
    if ((head) == None):
        (head) = temp
    else:
        temp.next = head
        (head).prev = temp
        (head) = temp
    return head
head = None

head = insert(head, 9)
head = insert(head, 8)
head = insert(head, 6)
head = insert(head, 5)
head = insert(head, 4)
head = insert(head, 2)
head = insert(head, 1)

x = 15
display(head)

print("arr : ", countTriplets(head, x))
