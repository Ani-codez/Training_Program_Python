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

    def enter(self,data):
        new=Node(data)
        if self.is_empty():
            self.head=new
        else:
            current=self.head
            while(current.next is not None):
                current=current.next
            current.next=new

    def printList(self):
        if self.is_empty():
            print("Empty")
        else:
            current=self.head
            while(current is not None):
                print(current.data)
                current=current.next
            
l=SLinkedList()
ip=input().split(",")
for i in ip:
    l.enter(i)
l.printList()
print("---------------")
