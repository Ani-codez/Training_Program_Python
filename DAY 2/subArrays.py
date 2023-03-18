n=int(input())
l=list(map(int,input().split()))
count=0
for i in range(len(l)):
    for j in range(i,len(l)):
        print(l[i:j+1], end=" ")
        if sum(l[i:j+1])%2!=0:
            count+=1
print()
print(count)
