class node:
    def __init__(self, da):
        self.data = da
        self.next = None

def display(head):
    while (head != None):
        # print(head.data, "\t\t\t\t\t\t\t|", head, head.next)
        print(head.data,end=' ')
        head = head.next
    print("")

def array_to_linked(arr):
    head = None
    for i in range(len(arr)):
        if head == None:
            nod = node(arr[i])
            head = nod
        else:
            p = head
            while (p.next != None):
                p = p.next
            nod = node(arr[i])
            p.next = nod
    return head
#-------------------------------------------------------ye function mid nikal ke de dega
def mid(head):
    if head==None:
        return head
    hare=head
    tort=head
    while (hare.next!=None and hare.next.next!=None):
        hare=hare.next.next
        tort=tort.next
    return tort
#------------------------------------------------ye fubnction tab tak recursively call karta rahega jab tak sab single element me na
#------------------------bath jaye  uske baad ye data ke hisab se sort hokar merging operation suru kar dega------------------------
def mergesort(hea):
    if hea==None or  hea.next==None:
        return hea                    #this is my base case of recurion to be sttoped

    middle=mid(hea)
    nxtmid=middle.next
    middle.next=None

    left=mergesort(hea)
    right=mergesort(nxtmid)
    sortedlist=merging(left,right)
    return sortedlist

def merging(head1,head2):
    res=None
    if head1==None:
        return head2
    if head2==None:
        return head1

    if head1.data<=head2.data:
        res=head1
        res.next=merging(head1.next,head2)
    else:
        res=head2
        res.next=merging(head1,head2.next)
    return res

if __name__ == '__main__':
    arr = [5,3,7,2,1,8,3,9,4]
    print("----------------ORIGINAL DATA---------------------------------")
    head = array_to_linked(arr)
    display(head)
    # print(mid(head).data)
    head=mergesort(head)
    display(head)
