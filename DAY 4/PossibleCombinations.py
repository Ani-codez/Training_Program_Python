def find_sum(SUM, List):
    if SUM == 0:
        return [[]]
    if not List:
        return []
    res = []
    for i in range(len(List)):
        if List[i] <= SUM:
            sub_res = find_sum(SUM - List[i], List[i:])
            for sub in sub_res:
                res.append([List[i]] + sub)
    return res

SUM = int(input())
List = list(map(int,input().split()))
result = find_sum(SUM, List)
print(result,len(result))
