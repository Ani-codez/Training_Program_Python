def linear_search(array,n,x):
    for i in range(0,n):
        if array[i]==x:
            return i
    return -1

array=[2,4,5,0,8,1,9]
x=5
n=len(array)
res=linear_search(array,n,x)
print("Not found") if res==-1 else print("Found at",res)
