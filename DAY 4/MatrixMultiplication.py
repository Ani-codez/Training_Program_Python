r,c=map(int,input().split())
r2,c2=map(int,input().split())
a=[]
b=[]
x=[]
for i in range(r):
    a.append(list(map(int,input().split())))

for i in range(r2):
    b.append(list(map(int,input().split())))

for i in range(r):
    x.append([0]*c2)
print(x)
if r!=c2:
    print("Not possible")
else:
    for i in range(r):
        for j in range(c2):
            for k in range(c):
                x[i][j]+=(a[i][k]*b[k][j])
print(x)
