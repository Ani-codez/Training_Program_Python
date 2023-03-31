class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class SLinkedList:
    def __init__(self):
        self.head=None

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def push(self,val):
        new=Node(val)
        if self.head is None:
            self.head=new
        else:
            new.next=self.head
            self.head=new

    def printL(self):
        current=self.head
        while(current is not None):
            print(current.data)
            current=current.next

    def make_distinct(self):
        current=self.head
        while(current.next is not None):
            if current.next.data==current.data:
                current.next=current.next.next
                continue
            current=current.next
        
l=SLinkedList()
print(l.is_empty())
l.push(50)
l.push(40)
l.push(30)
l.push(30)
l.push(30)
l.push(20)
l.push(20)
l.push(10)
l.push(10)
l.printL()
l.make_distinct()
l.printL()
