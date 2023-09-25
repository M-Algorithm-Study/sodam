# 백준 / 21736번 헌내기는 친구가 필요해(공통)

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
campus =  list(input().strip() for _ in range(n))
dir = [(1,0), (0,1), (-1,0), (0,-1)]
visit = [[0]*m for _ in range(n)]
que = deque()
cnt = 0

# 시작점인 도연이를 찾아 que 에 담아주고 시작
for x in range(n):
  for y in range(m):
    if campus[x][y] == 'I':
      que.append((x,y))
      visit[x][y] = 1

# bfs로 갈 수 있는 영역에서 만나는 p(사람) 수를 확인하여 +1
while que:
  x, y = que.popleft()
  for d in dir:
    dx, dy = x+d[0], y+d[1]
    
    if 0<=dx<n and 0<=dy<m:
      # 범위 내 벽도 아니고 방문을 안한 경우
      if campus[dx][dy] != 'X' and visit[dx][dy] != 1:
        que.append((dx,dy))
        visit[dx][dy] = 1
        # 근데 그게 사람일 경우 cnt +1
        if campus[dx][dy] == 'P':
          cnt += 1

# 만날 수 있는 P 의 수가 0 이면 TT 아니면 cnt 출력                    
print(cnt if cnt > 0 else 'TT')