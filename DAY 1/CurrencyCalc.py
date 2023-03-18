need=int(input())
curr=input()
if curr=="euro":
    print(need*0.01417)
elif curr=="british pound":
    print(need*0.01)
elif curr=="australian dollar":
    print(need*0.02140)
elif curr=="canadian dollar":
    print(need*0.02027)
else:
    print(-1)
