# 백준 / 15654번 N과 M(5) (공통)

# from itertools import permutations
# n,m= map(int,input().split())
# num = sorted(list(map(int,input().split())))

# for i in permutations(num,m):
#     print(*i)

n,m = map(int,input().split())
lst = sorted(list(map(int,input().split())))
num = []

def dfs():
    if len(num) == m:
        print(*num)
        return
    for i in lst:
        if i not in num:
            num.append(i)
            dfs()
            num.pop()
dfs()