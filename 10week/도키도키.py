# 백준 / 12789번 도키도키 간식드리미

from collections import deque
n = int(input())
q = deque(map(int,input().split()))
s = deque()
cnt = 1

while q:
    if q and q[0] == cnt:
        q.popleft()
        cnt += 1
    else:
        s.append(q.popleft())
    while s and s[-1] == cnt:
        s.pop()
        cnt += 1
print('Sad' if s else 'Nice')