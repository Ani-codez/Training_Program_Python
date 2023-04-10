class Bakehouse:
    def __init__(self,occupied_table_list):
        self.occupied_list=occupied_table_list

    def occupied_tables_list(self):
        current=self.occupied_list.head
        while(current is not None):
            if current.data[1]==True:
                print(current.data[0],end=" ")
            current=current.next

    def allocate_table(self):
        current=self.occupied_list.head
        i=1
        while i<11 and current is not None:
            if current.data[1]==False:
                current.data[1]=True
                print("Table",i,"allocated!")
                return current.data[0]
            current=current.next
            i+=1
        return -1

    def deallocate_table(self,data):
        current=self.occupied_list.head
        while current is not None:
            if current.data[0]==data:
                current.data[1]=False
                print("Table",data,"Deallocated!")
            current=current.next
    
class Table:
    def __init__(self,data):
        self.data=data
        self.next=None

class Link:
    def __init__(self):
        self.head=None

    def is_empty(self):
        if self.head==None:
            return True
        return False

    def insert(self,data):
        if self.head==None:
            self.head=Table(data)
        else:
            current=self.head
            while(current.next is not None):
                current=current.next
            current.next=Table(data)

table=Link()

for i in range(1,11):
    table.insert([i,False])

bake=Bakehouse(table)
bake.occupied_tables_list()
print("-----")
bake.allocate_table()
bake.occupied_tables_list()
print()
bake.deallocate_table(1)
bake.occupied_tables_list()
