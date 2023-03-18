n=int(input())
if n%3==0:
    print("Multiple of 3 and 5") if (n%5==0) else print("Multiple of 3")
elif n%5==0:
        print("Multiple of 5")
else:
    print("Invalid")

print("3,5") if not(n%3 and n%5) else (print(3) if not(n%3) else (print(5) if not(n%5) else print("Invalid")))
