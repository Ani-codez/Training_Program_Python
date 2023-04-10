class Queue:
    def __init__(self,size):
        self.size=size
        self.front=0
        self.rear=-1
        self.array=[None]*self.size

    def is_empty(self):
        if self.front>self.rear:
            return True
        return False

    def is_full(self):
        if self.rear==self.size-1:
            return True
        return False

    def enqueue(self,data):
        if self.is_full():
            print("Full")
        else:
            self.rear+=1
            self.array[self.rear]=int(data)

    def dequeue(self):
        if self.is_empty():
            print("Empty")
        else:
            self.front+=1
            return self.array[self.front-1]

    def display(self):
        if self.is_empty():
            print("EMpty")
        else:
            for i in range(self.front,elf.rear+1):
                print(self.array[i])

class Stack:
    def __init__(self,size):
        self.size=size
        self.array=[None]*self.size
        self.top=-1

    def is_empty(self):
        if self.top==-1:
            return True
        return False

    def is_full(self):
        if self.top==self.size-1:
            return True
        return False

    def push(self,data):
        if self.is_full():
            print("Full")
        else:
            self.top+=1
            self.array[self.top]=data

    def pop(self):
        if self.is_empty():
            print("Empty")
        else:
            self.top-=1
            return self.array[self.top+1]

    def display(self):
        if self.is_empty():
            print("Empty")
        else:
            for i in range(self.top+1):
                print(self.array[i],end=" ")

n=int(input("Size of Queue:"))
q=Queue(n)
s=Stack(n)
list(map(q.enqueue,input("Enter Elements").split()))
for i in range(n//2):
    x=q.dequeue()
    tx=q.dequeue()
    if sum(range(x+1))==tx:
        s.push(tx)
    
s.display()
