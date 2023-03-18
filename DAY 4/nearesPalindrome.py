def palindrome(n):
    return (str(n)[::-1]==str(n))

n=int(input())
i=1
while True:
    if palindrome(n+i):
        print(n+i)
        break
    i+=1
