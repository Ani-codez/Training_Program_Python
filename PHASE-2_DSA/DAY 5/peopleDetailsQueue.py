class People:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender():
        return self.gender

class Queue:
    def __init__(self,size):
        self.rear=-1
        self.front=0
        self.size=size
        self.array=[None]*self.size
        
    def is_empty(self):
        if self.rear<self.front:
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
            self.array[self.rear]=data

    def dequeue(self):
        if self.is_empty():
            print("Empty")
        else:
            self.front+=1
            return self.array[self.front-1]

    def display(self,gender):
        for i in range(self.front,self.rear+1):
            if self.array[i].gender==gender:
                print(self.array[i].name,self.array[i].age,self.array[i].gender)

n=int(input("Enter No of Peoples:"))
Q=Queue(n)
P1=People("Ani","23","M")
P2=People("Bun","22","M")
P3=People("Sri","10","F")
P4=People("Sup","13","F")
P5=People("Sil","23","F")
l=[P1,P2,P3,P4,P5]
list(map(Q.enqueue,l))
Q.display(input("Gender(M/F):"))
