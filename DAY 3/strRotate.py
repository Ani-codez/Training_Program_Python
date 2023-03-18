s=input().split(',')

for i in s:
    l=i.split(":")
    sumDigits=sum(list(map(int,list(l[1]))))
    sumSqr=sum([int(i)**2 for i in l[1]])
    if sumSqr%2==0:
        print(l[0][-1]+l[0][0:len(l[0])-1])
    else:
        print(l[0][2:]+l[0][:2])
        

