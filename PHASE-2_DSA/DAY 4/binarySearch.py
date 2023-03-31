def binarySearch(array,key,low,high):
    while(low<=high):
        mid=low+(high-low)//2
        if array[mid]==key:
            return mid
        elif array[mid]>key:
            high=mid-1
        else:
            low=mid+1
    return -1
array=[1,2,3,4,5,6,7,90]
key=7
res=binarySearch(array,key,0,len(array)-1)
print(res)
