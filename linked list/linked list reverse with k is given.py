
class node:
    def __init__(self, da):
        self.data = da
        self.next = None

class linked:

    def display(head):
        while (head != None):
            print(head.data,end=" ")
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

    def reverse(head,k):
        p = head
        prev = None
        nxt=None
        c = 0
        while (p != None and c<k):
            nxt = p.next
            p.next = prev

            prev = p
            p = nxt
            c+=1
        # if head!=None:
        #     print(head.data)
        # else:
        #     print("NAN")
        if (head!=None):
            head.next=obj.reverse(nxt,k)
        return prev

if __name__ == '__main__':
    obj = linked
    arr = [1, 2, 3, 4, 5,6,7,8,9,11]
    print("----------------ORIGINAL DATA---------------------------------")
    head = obj.array_to_linked(arr)
    obj.display(head)

    rev=obj.reverse(head,3)
    obj.display(rev)