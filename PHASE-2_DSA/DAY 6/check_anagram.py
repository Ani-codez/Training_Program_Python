def check_anagram(s,s1):
    if len(s)!=len(s1):
        return False
    for i,j in zip(s,s1):
        if i==j:
            return False
    if sorted(s)==sorted(s1):
        return True

s=input()
s1=input()
print(check_anagram(s.lower(),s1.lower()))
