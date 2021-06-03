# Python3 code to move the last item to front
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Function to add a node
    # at the beginning of Linked List
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Function to print nodes in a
    # given linked list
    def printList(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end=", ")
            tmp = tmp.next
        print()

    # Function to bring the last node to the front
    def moveToFront(self):
        p=self.head
        prev=None
        while p.next!=None :
            prev=p
            p=p.next
        nod=p
        prev.next=None
        p.next=self.head
        self.head=nod
        return self.head




if __name__ == '__main__':
    llist = LinkedList()

    # swap the 2 nodes
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    llist.push(8)
    print("Linked List before moving last to front ")
    llist.printList()
    llist.moveToFront()
    print("Linked List after moving last to front ")
    llist.printList()
