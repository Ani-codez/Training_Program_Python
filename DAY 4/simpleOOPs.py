'''
class Example:
    def __init__(self,num):
        self.num=num
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num

obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())
'''
########################################
'''
class Book:
    def __init__(self):
        self.title=None

my_fav=Book()
my_fav.title="This Book"
your_fav=Book()
your_fav.title="IDK=="

my_fav.title="Updated"

print("My fav:=",my_fav.title,"\nYour fav:=",your_fav.title)
'''
##########################################
"""
class Shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material

    def __str__(self):
        return "Price:"+str(self.price)+"Material:"+self.material

s1=Shoe(1000,"Canvas")
print(s1)
print(s1.price,s1.material)
"""
#########################################
'''
class Mobile:
    def display(self):
        print("Displayin:")

    def purchase(self):
        self.display()
        print("calculating")
Mobile().purchase()
'''
##################################################
'''
class Customer:
    def __init__(self,custid,name,balance):
        self.custid=custid
        self.name=name
        self.balance=balance
    def update(self,amt):
        self.balance+=amt
    def show(self):
        return ("balance:",self.balance)

c1=Customer(100,"Gopu",1000)
print(c1.show())
'''
#############################################
class Table:
    def __init__(self):
        self.no_legs=4
        self.glassTop=None
        self.woodenTop=None
    /
diningTable=Table()
backTable=Table()
frontTable=backTable
backTable=diningTable
print(diningTable,backTable,frontTable)
