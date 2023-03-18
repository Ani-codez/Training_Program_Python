list1=[20,10,90,11]
list1.insert(1,122)
list1.extend([10])
print(list1)
list1.pop() #index \--default removes last val
print(list1)

list1.remove(10) #value
print(list1)

del list1[2]
print(list1)
