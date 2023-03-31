class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def is_empty(self):
        if self.head==None:
            return True
        return False

    def length(self):
        point=self.head
        count=0
        while(point is not None):
            count+=1
            point=point.next
        return count

    def printList(self):
        val=self.head
        while(val is not None):
            print(val.data)
            val=val.next

    def insert_start(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode

    def insert_end(self,data):
        newNode=Node(data)
        if self.is_empty():
            self.head=newNode
        else:
            current=self.head
            while(current.next is not None):
                current=current.next
            current.next=newNode
            newNode.prev=current

    def insert_pos(self,data,pos):
        newNode=Node(data)
        if self.head is None and pos>0:
            print("Empty list!")
        elif pos==0:
            newNode.next=self.head
            self.head=newNode
        else:
            count=0
            current=self.head
            while(count<pos and current is not None):
                count+=1
                current=current.next
            current.prev.next=newNode
            newNode.prev=current.prev
            newNode.next=current

    def del_start(self):
        if self.head is None:
            print("Empty!")
        else:
            self.head=self.head.next
            self.head.prev=None

    def del_last(self):
        if self.head is None:
            print("Empty")
        else:
            current=self.head
            while(current.next is not None):
                current=current.next
            current.prev.next=None
            current.prev=None

    def del_position(self,pos):
        if self.head==None:
            print("Empty")
        elif(pos==0):
            self.del_start()
        elif(pos==self.length()-1):
            self.del_last()      
        else:
            current=self.head
            for i in range(pos):
                current=current.next
            current.prev.next=current.next
            current.next.prev=current.prev
            current.prev=None
            current.next=None
        
dl=DoublyLinkedList()
print(dl.is_empty())
print("--------------")
dl.insert_start("x")
dl.insert_start("zzz")
dl.printList()
print("--------------")
dl.insert_start("Z")
dl.printList()
print(dl.length())
print("--------------")
dl.insert_end("A")
dl.printList()
print("--------------")
dl.insert_pos(5,1)
dl.printList()
print("--------------")
dl.del_start()
dl.printList()
print("--------------")
dl.del_last()
dl.printList()
print("--------------")
dl.del_position(1)
dl.printList()
