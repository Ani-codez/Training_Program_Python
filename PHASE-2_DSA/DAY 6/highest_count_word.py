text=input().split()
d={}
try:
    for i in text:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    if list(d.values()).count(max(d.values()))>1:
        long=0
        string=""
        for i in d:
            if d[i]==max(d.values()) and len(i)>long:
                long=len(i)
        for i in d:
            if len(i)>=long:
                print(i,d[i])
    else:
        [print(i) for i in d if d[i]==max(d.values())]
except:
    print("Invalid Input")
