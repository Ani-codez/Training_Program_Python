#shorthand
'''
[print(i) for i in range(0,10,2)]
l=[]
[l.append(i) if i<5 else l.append(i**2) for i in range(10)]
print(l)
[l.append(i) for i in range(10) if i<5]
print(l)
'''
##########################################################

mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
power=[]
for i in mat:
    l=[]
    [l.append(j**2) if j%2!=0 else l.append(j**3) for j in i] 
    power.append(l)

print(power)

################################################3

[print(i**3) if i%2==0 else print(i**2) for j in mat for i in j]

##################################################
