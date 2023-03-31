class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__front=0
        self.__rear=-1

    def is_empty(self):
        if self.__rear==-1 or self.__front==self.get_max_size():
            return True 
        else:
            return False

    def is_full(self):
        if self.__rear==self.__max_size-1:
            return True
        return False

    def enqueue(self,data):
        if self.is_full():
            print("Queue Full")
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

    def get_max_size(self):
        return self.__max_size

integerQ=Queue(3)
stringQ=Queue(6)
resultQ=Queue(integerQ.get_max_size()+stringQ.get_max_size())
for i in range(integerQ.get_max_size()):
    integerQ.enqueue(int(input()))

for i in range(stringQ.get_max_size()):
    stringQ.enqueue(input())

for i in range(max(integerQ.get_max_size(),stringQ.get_max_size())):
    if i<min(integerQ.get_max_size(),stringQ.get_max_size()):
        resultQ.enqueue(integerQ.dequeue())
        resultQ.enqueue(stringQ.dequeue())
    else:
        resultQ.enqueue(stringQ.dequeue()) if integerQ.is_empty() else resultQ.enqueue(integerQ.dequeue())
resultQ.display()
