class Vehicle:
    def __init__(self,vehicleID,type,cost):
        self.__vehicleID=vehicleID
        self.__type=type
        self.__cost=cost

    def premium(self):
        if self.__type==2:
            return self.__cost*0.02
        else:
            return self.__cost*0.06

    def display(self):
        premiumamt=self.premium()
        print("VehicleID:",self.get_id())
        print("Type:",self.get_type())
        print("Cost:",self.get_cost())
        print("Premium Amount:",premiumamt)
        return ""

    def set_id(self,id):
        self.__vehicleID=id
    def get_id(self):
        return self.__vehicleID

    def set_type(self,type):
        self.__type=type
    def get_type(self):
        return self.__type

    def set_cost(self,cost):
        self.__cost=cost
    def get_cost(self):
        return self.__cost
    
p1=Vehicle(102,2,20000)
p1.set_id(120)
print(p1.get_id())
print(p1.display())
