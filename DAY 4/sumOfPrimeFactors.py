
def isPrime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1

n=int(input())
large=0 ##sum of the PRIME factors
factor=0

for i in range(n,n+9): 
    if isPrime(i):
        large+=i
    else:        
        factor=j for j in range(2,i//2+1) if isPrime(j) and i%j==0  
        large+=factor
print(large)
            
        
