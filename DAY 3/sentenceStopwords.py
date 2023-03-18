sentences=["a new world record was set",
           "in the holy city of ayodhya",
           "on the eve of diwali on teusday",
           "with over three lakhs diya or earthen lamps",
           "lit up simultaneously on the bank of river sarayu river"]
stopwords=["for","a","of","the","and","to","in","on","with"]

for i in sentences:
    for j in i.split():
        if j not in stopwords:
            print(j,end=" ")
    print()

print("\n\n")

[print(j,end=" ") for i in sentences for j in i.split() if j not in stopwords]

print("\n\n")

s=" ".join(sentences)
[print(i,end=" ") for i in s.split() if i not in stopwords]
