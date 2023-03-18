mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
tip=[]
d={}
for i in list_b:
    tip.append((i,mylist.index(i)))
    d[i]=mylist.index(i)
print(tip)
print(d)
