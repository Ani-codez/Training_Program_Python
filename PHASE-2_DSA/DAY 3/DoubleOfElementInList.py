l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
new=[]
for i in l1:
    if i*2 in l2:
        new.append(i)
print(new)
