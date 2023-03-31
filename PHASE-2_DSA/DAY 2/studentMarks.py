marks=list(map(int,input().split()))
#inserting marks which is not entered
m,p=map(int,input("Enter Marks and Position").split())
marks=marks[:p-1]+[m]+marks[p:] if p!=1 else [m]+marks[:]
print(marks)
#Print data at 5 AND 7
print(marks[4],marks[6])
