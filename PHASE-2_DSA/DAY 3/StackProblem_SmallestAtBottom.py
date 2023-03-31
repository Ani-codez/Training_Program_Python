class Stack:
    def __init__(self,size):
        self.top=-1
        self.len=size
        self.array=[None]*size
        
    def is_empty(self):
        if self.top==-1:
            return True
        return False

    def is_full(self):
        if self.top==self.len-1:
            return True
        return False

    def push(self,data):
        if self.is_full():
            print("FUll")
            return
        self.top+=1
        self.array[self.top]=data

    def pop(self):
        self.top-=1
        return self.array[self.top+1]

    def smallToBottom(self):
        small=min(self.array)
        ct=self.top
        hold=[]
        while(ct>=0):
            hold.append(self.pop())
            ct-=1
        for i in [small]*hold.count(small):
            self.push(i)
        for i in hold[::-1]:
            if i!=small:
                self.push(i)
            
    def display(self):
        ct=self.top
        while(ct>=0):
            print(self.array[ct])
            ct-=1

s=Stack(5)
s.push(7)
s.push(8)
s.push(5)
s.push(66)
s.push(5)
s.display()
print("---------")
s.smallToBottom()
s.display()
