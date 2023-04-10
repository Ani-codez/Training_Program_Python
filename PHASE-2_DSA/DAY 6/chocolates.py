child_id=tuple(map(int,input().split()))
chocolates=list(map(int,input().split()))

def calculate_total_chocolates():
    return sum(chocolates)

def reward_child(id,extra_chocolates):
    if extra_chocolates<1:
        print("Extra chocolates is less than 1")
    elif id not in child_id:
        print("Child id is invalid")
    else:
        chocolates[child_id.index(id)]=chocolates[child_id.index(id)]+extra_chocolates
        print("Chocolates Rewarded!\n",*chocolates)

print("Total Rewards:",calculate_total_chocolates())
reward_child(30,5)
print("After Updating..\nTotal Rewards:",calculate_total_chocolates())
