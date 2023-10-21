# 백준 / 2565번 전깃줄(공통)

import sys
input = sys.stdin.readline

n = int(input())
# 연결 가능한 전깃줄의 수 (최소 1개)
ans = [1]*n
line = sorted([list(map(int,input().split())) for _ in range(n)])

# 오름차순으로 정렬하고 이전에 연결된 전깃줄의 위치 숫자보다 클 경우에만 +1
for i in range(1,n):
    for j in range(0,i):
        if line[i][0]>line[j][0] and line[i][1]>line[j][1]:
            ans[i]=max(ans[i],ans[j]+1)

print(n-max(ans))
