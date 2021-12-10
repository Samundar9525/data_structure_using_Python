class node:
    def __init__(self, da):
        self.data = da
        self.next = None


class linked:

    def display(head):
        while (head != None):
            print(head.data, "\t\t\t\t\t\t\t|", head, head.next)
            head = head.next

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

    def reverse(head):
        p = head
        prev = None
        while (p != None):
            nxt = p.next
            p.next = prev
            prev = p
            p = nxt
        return prev


    def recur(nod):
        if nod == None:
            return nod
        if nod.next == None:
            return nod

        head = obj.recur(nod.next)
        nod.next.next = nod
        nod.next = None
        return head


if __name__ == '__main__':
    obj = linked
    arr = [1, 2, 3, 4, 5]
    print("----------------ORIGINAL DATA---------------------------------")
    head = obj.array_to_linked(arr)
    obj.display(head)
    print("----------------REVERSE BY ITERATION ------------------------")
    rev_by_iter=obj.reverse(head)
    obj.display(rev_by_iter)
    print("---------------REVERSE BY Rcursion --------------------------")
    rev_by_recur = obj.recur(rev_by_iter)
    obj.display(rev_by_recur)
