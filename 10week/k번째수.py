# 백준 / 11004번 k번째수

n,m = map(int,input().split())
lst = sorted(list(map(int,input().split())))
print(lst[m-1])
