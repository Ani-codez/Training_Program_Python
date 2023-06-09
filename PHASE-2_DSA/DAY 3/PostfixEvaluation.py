class Evaluate:
    def __init__(self,capacity):
        self.top=-1
        self.capacity=capacity
        self.array=[]

    def is_empty(self):
        return self.top==-1

    def peek(self):
        return self.array[-1]

    def pop(self):
        if not self.is_empty():
            self.top-=1
            return self.array.pop()
        else:
            return "$"

    def push(self,op):
        self.top+=1
        self.array.append(op)

    def evaluate(self,exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                val1=self.pop()
                val2=self.pop()
                self.push(str(eval(val2+i+val1)))
        return int(self.pop())

exp="231*+9-"
obj=Evaluate(len(exp))
print("Answer:",obj.evaluate(exp))
