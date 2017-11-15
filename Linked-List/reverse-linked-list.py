""" Reverse a Singly linked list"""


class Node:
    def __init__(self, data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    def push(self, item):
        temp=Node(item)
        temp.next=self.head
        self.head=temp

    def printList(self):
        temp=self.head
        while temp:
            print (temp.data)
            temp=temp.next

    def reverse(self, head):
        previous=None
        while head:
            current=head
            head=head.next
            current.next=previous
            previous=current
        return previous




head= Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)

#LinkedList().printList()

print(LinkedList().reverse(head))

#LinkedList().printList()

