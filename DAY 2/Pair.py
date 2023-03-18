'''*l,n=list(map(int,input().split()))
count=0
for i in range(len(l)):
    if l[i]==float('INF'):
        continue
    for j in range(i+1,len(l)):
        if l[i]+l[j]==n:
            count+=1
            print(l[i],l[j])
            l[j]=float('INF')
            break
        else:
            continue
print(count) if count>0 else print(0)
'''

###########################################333

*l,n=list(map(int,input().split()))
l.sort()
count=0
start=0
end=l.index(l[-1])
while(start<end):
    if l[start]+l[end]==n:
        count+=1
        start+=1
        end-=1
    elif l[start]+l[end]<n:
        start+=1
    elif l[start]+l[end]>=n:
        end-=1
    
print(count)

