class Compartment:
    def __init__(self,name,passengers,total_capacity):
        self.name=name
        self.passengers=passengers
        self.total_capacity=total_capacity
        self.next=None

class LinkCompartment:
    def __init__(self):
        self.head=None

    def is_empty():
        if self.head is None:
            return True
        return False

    def add(self,data):
        new=Node(data)
        if self.is_empty():
            self.head=new
        else:
            current=self.head
            while(current.next is not None):
                current=current.next
            current.next=new

    def printList(self):
        current=self.head
        while(current is not None):
            print(current.data)
            current=current.next
    
class Train:
    def __init__(self,train_name,compartment_list):
        self.train_name=train_name
        self.compartment_list=compartment_list

    def get_train_name(self):
        return self.train_name

    def get_compartment_list(self):
        return self.compartment_list

    def count_compartments(self):
        current=self.compartment_list.head
        count=0
        while(current is not None):
            count+=1
            current=current.next
        return count

    def check_vacancy(self):
        current=self.compartment_list.head
        count=0
        while current is not None:
            if current.passengers<0.5*current.total_capacity:
                count+=1
            current=current.next
        return count
    
c1=Compartment("SL",250,400)
c2=Compartment("2AC",125,280)
c3=Compartment("3AC",120,300)
c4=Compartment("FC",160,300)
c5=Compartment("1AC",100,210)

l=LinkCompartment()
l.head=c1
c1.next=c2
c2.next=c3
c3.next=c4
c4.next=c5

T=Train("ni",l)
print(T.count_compartments())
print(T.check_vacancy())
