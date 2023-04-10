def selectionSort(array,size):

    for i in range(0,size):
        min_idx=i

        for j in range(i+1,size):
            if array[j]<array[i]:
                min_idx=j

        array[min_idx],array[i]=array[i],array[min_idx]

array=list(map(int,input().split()))
selectionSort(array,len(array))
print(array)
