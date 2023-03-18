x=int(input())
y=int(input())
z=int(input())

a=z/5
if a>=x:
    z-=(x*5)
    
    if z<=y:
        print(x,z)
    else:
        print(-1)
else:
    r5=z/5
    z-=(z/5)
    if z<=y:
        print(r5,z)
    else:
        print(-1)
    
