# 백준 / 9251번 LCS (공통)

import sys
input = sys.stdin.readline
n = input().strip()
m = input().strip()
lst = [0] * len(m)

for i in range(len(n)):
    cnt = 0
    for j in range(len(m)):
        if cnt < lst[j]:
            cnt = lst[j]
        elif n[i] == m[j]:
            lst[j] = cnt + 1
print(max(lst))


# 아직 이해가 잘 안됐어요 ....