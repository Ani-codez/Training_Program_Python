class Queue:
    def __init__(self,size):
        self.size=size
        self.rear=-1
        self.front=0
        self.array=[None]*self.size

    def is_empty(self):
        if self.rear<self.front:
            return True
        return False

    def is_full(self):
        if self.rear==self.size-1:
            return True
        return False

    def display(self):
        if self.front<=self.rear:
            for i in range(self.front,self.rear+1):
                print(self.array[i],end=" ")

    def enqueue(self,data):
        if self.is_full():
            print("Full")
        else:
            self.rear+=1
            self.array[self.rear]=data

    def dequeue(self):
        if self.is_empty():
            print("Full")
        else:
            self.front+=1
            return self.array[self.front-1]
n=int(input("Enter Size of Queue"))
InpQ=Queue(n)
OddQ=Queue(n)
EvenQ=Queue(n)
inputQ=list(map(int,input().split()))
[InpQ.enqueue(i) for i in inputQ]
InpQ.display()
print("\n----------")
for i in range(n):
    x=InpQ.dequeue()
    if x%2==0:
        EvenQ.enqueue(x)
    else:
        OddQ.enqueue(x)
print("Even Queue:")
EvenQ.display()
print("\nOdd Queue:")
OddQ.display()
