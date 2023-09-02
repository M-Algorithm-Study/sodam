# 백준 / 11722번 가장 긴 감소하는 부분 수열

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))

ans = [1 for _ in range(n+1)]

for i in range(n):
  for j in range(i):
    if lst[i] < lst[j]:
      ans[i] = max(ans[i],ans[j]+1)
print(max(ans))