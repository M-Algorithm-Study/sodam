# 백준 / 1922번 네트워크 연결(공통)

import sys
import heapq
input = sys.stdin.readline

n = int(input())
visit = [0] * (n + 1)
computer = [[] for _ in range(n + 1)]
queue = [(0, 1)]

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    computer[a].append((c, b))
    computer[b].append((c, a))

total,cnt = 0, 0
while queue and cnt < n:
    cost, com = heapq.heappop(queue)
    if not visit[com]:
        visit[com] = 1
        total += cost
        cnt += 1
        for i in computer[com]:
            # heapq 를 사용하여 비용이 더 조금 드는 경우를 먼저 방문 처리 할 수 있다.
            heapq.heappush(queue, (i[0], i[1]))
print(total)