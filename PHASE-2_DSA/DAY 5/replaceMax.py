import random
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Link:
    def __init__(self):
        self.head=None

    def insert(self,data):
        new=Node(int(data))
        if self.head==None:
            self.head=new
        else:
            current=self.head
            while(current.next is not None):
                current=current.next
            current.next=new

    def printlist(self):
        if self.head==None:
            print("None")
        else:
            current=self.head
            while current is not None:
                print(current.data)
                current=current.next

    def max(self):
        if self.head==None:
            return None
        else:
            maxx=-float('INF')
            current=self.head
            while current is not None:
                if current.data>maxx:
                    maxx=current.data
                current=current.next
        return maxx

    def change_max(self):
        maxx=self.max()
        current=self.head
        while current is not None:
            if current.data==maxx:
                current.data=random.randint(0,100)
            current=current.next
l=Link()
list(map(l.insert,input().split()))
l.printlist()
print("Max:",l.max())
print("-------------")
l.change_max()
l.printlist()
