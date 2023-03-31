class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLink:
    def __init__(self):
        self.head=None

    def insert(self,data):
        new=Node(int(data))
        if self.head is None:
            self.head=new
        else:
            current=self.head
            while(current.next is not None):
                current=current.next
            current.next=new

    def printList(self):
        if self.head==None:
            print(None)
        else:
            current=self.head
            while(current is not None):
                print(current.data,end="->")
                current=current.next

    def length(self):
        if self.head is None:
            return 0
        else:
            current=self.head
            count=0
            while(current is not None):
                count+=1
                current=current.next
            return count

    def merge(self,n,list2):
        current=self.head
        while(current is not None):
            if n==0:
                list2.printList()
            print(current.data,end="->")
            current=current.next
            n-=1
list1=SLink()
list2=SLink()
list(map(list1.insert,input().split()))
list(map(list2.insert,input().split()))

#list1.printList()
#list2.printList()

n=int(input())

list1.merge(n,list2)
