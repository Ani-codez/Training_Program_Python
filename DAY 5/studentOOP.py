class Student:
    def __init__(self,s_id,age,marks):
        self.__s_id=None
        self.__age=None
        self.__marks=None

    def validate_marks(self):
        if self.get_marks() >=0 and self.get_marks()<=100:
            return 1
        return 0

    def validate_age(self):
        if self.get_age()>20:
            return 1
        return 0

    def check_qualification(self):
        if self.validate_marks() and self.validate_age() and self.get_marks()>=65:
            print(self.fees())
            return True
        
        return False
      
    def fees(self):
        if self.check_qualification():
            dic={"Course 1001":25575.0,"Course 1002":15500.0}
            discount={"Course 1001":25575.0*0.75,"Course 1002":15500.0*0.75}
            print("Course List::")
            if self.get_marks()<=85:
                return (dic)
            else:
                return (discount)
        else:
            return "Not eligible for any course!"

    def set_id(self,id):
        self.__s_id=id
    def get_id(self):
        return self.__s_id

    def set_age(self,age):
        self.__age=age
    def get_age(self):
        return self.__age

    def set_marks(self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks

s1=Student(0,0,0)

s1.set_id(int(input("ID:")))
s1.set_age(int(input("Age:")))
s1.set_marks(int(input("Marks:")))
print(s1.fees())
print("Qualified? :",s1.check_qualification())

