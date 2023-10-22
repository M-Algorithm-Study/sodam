# 백준 / 2565번 전깃줄(공통)

import sys
input = sys.stdin.readline

n = int(input())
ans = [1]*n
line = sorted([list(map(int,input().split())) for _ in range(n)])

# 연결 가능한 전깃줄 수 확인 (오름차순으로 정렬하여 오른쪽 수가 큰 전깃줄) 
for i in range(n):
    for j in range(i):
        if line[i][1] > line[j][1]:
            ans[i] = max(ans[i],ans[j]+1)

print(n - max(ans))
