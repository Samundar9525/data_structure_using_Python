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
#-----------------------------linkedlist creation ends  here  ------------------------------------------------>
def merge(h1,h2):
    if h1==None:
        return h2
    if h2==None:
        return h1
    if h1.data>h2.data:
        h1,h2=h2,h1
    ans=h1
    while(h1!=None and h2!=None):
        prev=None
        while(h1!=None and h1.data<=h2.data):
            prev=h1
            h1=h1.next
        prev.next=h2
        h1,h2=h2,h1
    return ans

def recursive(h1,h2):
    if h1==None :
        return h2
    if h2==None:
        return h1
    if h1.data<=h2.data:
        res=h1
        res.next=recursive(h1.next,h2)
    else:
        res=h2
        res.next=recursive(h1,h2.next)
    return res

if __name__ == '__main__':
    arr = [1,3, 5, 7, 9]
    brr=[2,4,6,8,]
    print("----------------ORIGINAL DATA---------------------------------")
    head1 = array_to_linked(arr)
    head2=array_to_linked(brr)
    display(head1)
    display(head2)
    print("-------------------------------------")

    head3=merge(head1,head2)
    display(head3)

    # head4=recursive(head1,head2)
    # display(head4)

    print("end")