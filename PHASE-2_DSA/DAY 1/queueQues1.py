class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if (self.__max_size)-1==self.__rear:
            return True
        return False

    def is_empty(self):
        if self.__front>self.__rear:
            return True
        return False

    def enqueue(self,data):
        if self.is_full():
            print("Queue is Full!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if self.is_empty():
            print("Queue Empty!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        if self.is_empty():
            print("Queue Empty!")
        else:
            for index in range(self.__front,self.__rear+1):
                print(self.__elements[index])
n=int(input("Size of Queue:"))
ques=Queue(n)
ans=Queue(n)
print("Input Queue:")
size=n
while(size):
    ques.enqueue(int(input()))
    size-=1
for i in range(n):
    data=ques.dequeue()
    for j in range(1,11):
        if data%j==0:
            continue
        break
    else:
        ans.enqueue(data)
print("Output Queue")
ans.display()
