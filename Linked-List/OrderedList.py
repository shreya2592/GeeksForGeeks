# To implement an ordered List -- Doubly Linked List

from Node import Node


class OrderedList:
    def __init__(self):
        self.head=None

    def isEmpty(self):
        return self.head==None

    def add (self, item):
        current=self.head
        previous=None
        stop =False

        while current !=None and not stop:
            if current.getData()>item:
                stop =True
            else:
                previous=current
                current=current.getNext()

        temp=Node(item)
        if previous==None:
            temp.setNext(self.head)
            self.head=temp

        else:
            temp.setNext(current)
            previous.setNext(temp)



    def search(self, item):
        current=self.head
        found=False
        stop=False

        while current!=None and not found and not stop:
            if current.getData()==item:
                found=True
            else:
                if current.getData()>item:
                    stop=True
                else:
                    current=current.getNext()
        return found



    def size(self):
        count=0
        current=self.head
        while current !=None:
            count+=1
            current=current.getNext()
        return count

    def remove(self, item):
        previous=None
        current=self.head
        found= False

        while not found:
            if current.getData()==item:
                found =True
            else:
                previous=current
                current=current.getNext()

        if previous==None:
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext())
