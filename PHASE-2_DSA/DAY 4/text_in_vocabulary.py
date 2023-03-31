def found(text,vocabulary):
    l=[]
    for i in text:
        if i in vocabulary:
            l.append(i)
    return l
text=input().split()
vocabulary=input().split()
print(found(text,vocabulary))
