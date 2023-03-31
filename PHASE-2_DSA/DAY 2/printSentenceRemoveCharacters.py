class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Link:
    def __init__(self):
        self.head=None

    def insert(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
        else:
            current=self.head
            while(current.next is not None):
                current=current.next
            current.next=new

    def printlist(self):
        if self.head is None:
            print("Empty")
        else:
            current=self.head
            count=0
            while(current is not None):
                if current.data=="*" or current.data=="/":
                    print(" ",end=" ")
                    current=current.next
                    if current.data=="*" or current.data=="/":
                        current=current.next
                        print(current.data.upper(),end="")
                        current=current.next
                else:
                    print(current.data,end="")
                    current=current.next

l=Link()
s=input().split(",")
for i in s:
    l.insert(i)
l.printlist()
