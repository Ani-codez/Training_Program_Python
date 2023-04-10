class Fruit:
    fruit_name_list=["Apple","Guava","Orange","Grape","Sweet Lime"]
    fruit_price_list=[200,80,70,110,60]
    def __init__(self):
        pass

    def get_fruit_price(fruit_name):
        try:
            idx=fruit_name_list.index(fruit_name)
            return fruit_price_list[idx]
        except:
            return -1
        
class Purchase:
    counter=101
    def __init__(self):
        pass

    def calculate_price():
        
        
