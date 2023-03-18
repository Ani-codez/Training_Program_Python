'''#function
def pint():
    print("function printin")
pint()
def vibe(n1,n2):
    print("function vibin",n1,n2)
vibe(420,99)
def add(n1,n2):
    return n1+n2
print("value:",add(12,244.2))'''

#POSITIONAL ARGS

def position(num1,num2,num3):
    print(num1,num2,num3)

position(20,30,40)

#KEYWORD ARGS

def key(num1,num2,num3):
    print(num1,num2,num3)

key(num1=90,num3=11,num2=141)

#DEFAULT ARGS

def default(name,roll,branch="CSE"):
    print(name,roll,branch)

default("android",23)
default("xyz",233,"ECE")

#VARIABLE NO OF ARGS

def fun(*var):
    print(sum(var))
fun(10,20)
fun(20,30,10)
