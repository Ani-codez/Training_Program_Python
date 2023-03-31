list1=input().split()
list2=input().split()[::-1]
for i,j in zip(list1,list2):
    if i=="None" and j=="None":
        continue
    elif i=="None":
        print(j)
    elif j=="None":
        print(i)
    else:
        print(i+j)
        
#a app a d ke th doc awa
#y tor e eps ay None le n
