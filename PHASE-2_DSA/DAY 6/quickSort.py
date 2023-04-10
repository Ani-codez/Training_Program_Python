def partition(array,low,high):
    pivot=array[high]
    i=low-1
    for j in range(low,high):
        if array[j]<pivot:
            i+=1
            array[j],array[i]=array[i],array[j]
    array[i+1],array[high]=array[high],array[i+1]
    return i+1

def quicksort(array,low,high):
    if low<high:
        pi=partition(array,low,high)
        quicksort(array,low,pi-1)
        quicksort(array,pi+1,high)

data=list(map(int,input().split()))
quicksort(data,0,len(data)-1)
print(data)
