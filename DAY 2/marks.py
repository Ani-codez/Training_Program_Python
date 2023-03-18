def find_more_than_average(tup):
    average=sum(tup)/len(tup)
    count=0
    for i in tup:
        if (i>average):
            count+=1 
    print(count*10)
    
def generate_freq(tup):
    l=[]
    for i in range(0,26):
        l.append(tup.count(i))
    print(l)
    
def sort_marks(tup):
    print(sorted(list(tup)))
    
tup=tuple(map(int,input().split()))
find_more_than_average(tup)
generate_freq(tup)
sort_marks(tup)
