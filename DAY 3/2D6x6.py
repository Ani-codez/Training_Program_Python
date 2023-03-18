
"""
11 21 31 41 51 61
12 22 32 42 52 62
"""
mat=[]
for i in range(8):
    lis=[]
    for j in range(8):
        if i==0 or i==7 or j==0 or j==7:
            lis.append("----")
        else:
            lis.append([j,i])
    mat.append(lis)
    print(lis)
    print()

#print(mat)
