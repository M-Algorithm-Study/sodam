# 백준 / 2468번 안전영역 (공통)

from collections import deque
import sys
input = sys.stdin.readline

direct = [(1,0),(0,1),(-1,0),(0,-1)]

n = int(input())
field = [list(map(int,input().split())) for _ in range(n)]
num = 0

for high in range(101): # 높이는 1~100
  visit = [[0]*n for _ in range(n)]
  queue = deque()
  # 안전영역 카운트
  cnt = 0
  for i in range(n):
    for j in range(n):
      # 물의 높이 보다 높은 땅이면서 방문하지 않은 땅이면 카운트 +1
      if visit[i][j] == 0 and field[i][j] >= high:
        cnt += 1
        queue.append((i,j))
        # 시작점 기준 연결 되어있는 물의 높이보다 높은 땅 방문 처리
        while queue:
          x, y = queue.popleft()
          for d in direct:
            xd, yd = x+d[0], y+d[1]
            if 0 <= xd < n and 0 <= yd < n:
              if visit[xd][yd] == 0 and field[xd][yd] >= high:
                visit[xd][yd] = 1
                queue.append((xd, yd))
  # 물의 높이 마다 비교하면서 안전영역의 수가 더 많은 경우 확인
  num = max(num, cnt)
print(num)