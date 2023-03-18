class Customer:
    def __init__(self,quantity):
        self.quantity=quantity

    def validate_quantity(self):
        if self.quantity<=5 and self.quantity>=1:
            return True
        else:
            return False


class PizzaService(Customer):
    def __init__(self,quantity,type1,toppings):
        Customer.__init__(self,quantity)
        self.type=type1
        self.toppings=toppings
        self.cost=None

    def toppingsfn(self):
        return self.toppings
    
    def validate_pizza_type(self):
        if self.type=="small" or self.type=="medium":
            return True
        else:
            return False

    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and (self.quantity>1 and self.quantity<5):
            cost=0
            prices=[150,185,200,250]
            if self.type=="small":
                if self.toppingsfn():
                    cost=prices[1]
                else:
                    cost=prices[0]
            if self.type=="medium":
                if self.toppingsfn():
                    cost=prices[3]
                else:
                    cost=prices[2]
        self.cost=cost
        return cost
'''
class DoorDelivery(PizzaService):
    def __init__(self,distance):
        self.distance=distance

    def validate_distance(self):
        if self.distance>=1 and self.distance<=10:
            return True
        else:
            return False

    def pizza_cost(self):
        total_cost=-1
        if self.validate_distance() and self.calculate_pizza_cost()!=-1:
            deliveryCharge=0
            if self.distance>5:
                deliveryCharge=7
            else:
                deliveryCharge=5
            
            total_cost=self.calculate_pizza_cost()+deliveryCharge
        return total_cost
'''


p1=PizzaService(4,"small",True)
#d1=DoorDelivery(5)
#print(d1.pizza_cost())

print(p1.calculate_pizza_cost())
    
