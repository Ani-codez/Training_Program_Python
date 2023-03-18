s=input()
start=0
end=1
while end<len(s) and start<len(s):
    l=list(map(int,s[start:end+1]))
    if sum(l)==10:
        print(s[start:end+1])
        end+=1
    elif(sum(l)<10):
        end+=1
    else:
        start+=1


