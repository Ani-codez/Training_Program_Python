'''
3 numbers.. numbers to left of 7 ignore find product of rest 
l=list(map(int,input().split()))
product=1
if l[-1]==7:
    print(-1)
else:
    for i in l:
        if i==7:
            product=1
        else:
            product*=i
    print(product)'''
    
