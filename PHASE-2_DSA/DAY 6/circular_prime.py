def is_prime(n):
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return False
    return True

def circular_prime(n):
    n=str(n)
    l=[]
    if len(n)==1:
        return is_prime(int(n))
    else:
        for i in range(len(n)):
            l.append(n)
            n=n[1:]+n[0]
    for i in l:
        if is_prime(int(i)):
            continue
        else:
            return False
    else:
        return True

for i in range(2,int(input())):
    if circular_prime(i):
        print(i)
