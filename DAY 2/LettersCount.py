s=input()
letters=0
digits=0
for i in s:
    if i.isdigit():
        digits+=1
    elif i.isalpha():
        letters+=1
print([letters,digits])
