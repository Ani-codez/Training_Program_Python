class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def is_full(self):
        if (self.__max_size)-1==self.__top:
            return True
        return False

    def is_empty(self):
        if self.__top==-1:
            return True
        return False

    def push(self,data):
        if self.is_full():
            print("Stack is Full!")
        else:
            self.__elements[self.__top+1]=data
            self.__top+=1
            print("Data Entered Successfully!")

    def pop(self):
        if self.is_empty():
            print("Stack Empty!")
        else:
            data=self.__elements[self.__top]
            self.__top-=1
            return str(data)+"Popped"

    def display(self):
        if self.is_empty():
            print("Stack Empty!")
        else:
            idx=self.__top
            while(idx>-1):
                print(self.__elements[idx])
                idx-=1

    def get_max_size(self):
        return self.__max_size
n=int(input("Enter Size of Stack:\n0 to Exit:\n"))
stk=Stack(n)
choice=1
while(choice):
    choice=int(input("1.Push\n2.Pop\n3.Display\n4.Max Size\n5.Check If Empty\n6.Check If Full\n0.Exit\nEnter Your Choice:"))
    if choice==1:
        data=int(input("Enter Data to Enter:"))
        stk.push(data)
    elif choice==2:
        print(stk.pop())
    elif choice==3:
        stk.display()
    elif choice==4:
        print(stk.get_max_size())
    elif choice==5:
        print(stk.is_empty())
    elif choice==6:
        print(stk.is_full())
    elif choice==0:
        print("Thanks for Using!")
        break
    else:
        print("Invalid Input")
        break
    print("----------------------------------------------------------------------------------")
