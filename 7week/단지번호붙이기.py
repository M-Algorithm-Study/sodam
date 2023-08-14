# 백준 / 2667번 단지번호붙이기 (공통)

from collections import deque, Counter, defaultdict
import sys
input = sys.stdin.readline

n = int(input())
field = [list(map(int,input().strip())) for _ in range(n)]
visit = [[0]*n for _ in range(n)]
direct = [(1,0),(0,1),(-1,0),(0,-1)]
queue = deque()
cnt = 0

for a in range(n):
  for b in range(n):
    if field[a][b] == 1 and visit[a][b] == 0:
        # 필드를 순회하면서 단지 시작점을 만나면 카운트 +1 
        cnt += 1
        field[a][b] = cnt
        visit[a][b] = 1
        queue.append((a,b))
        # 단지 시작점에서 부터 연결 되어있는 집 체크
        while queue:
          x,y = queue.popleft()
          for d in direct:
            xd, yd = x + d[0], y + d[1]
            if 0 <= xd < n and 0 <= yd < n:
                if field[xd][yd] == 1 and visit[xd][yd] == 0:
                    # 이웃 된 집 방문 체크하면서 1을 단지번호로 변경
                    field[xd][yd] = cnt
                    visit[xd][yd] = 1
                    queue.append((xd,yd))
print(cnt) # 단지 수 출력

dic = defaultdict(int)
# 단지번호로 변경 된 필드를 순회 하면서 Counter 를 사용하여 
# 같은 단지번호인 집의 수를 딕셔너리에 더해줌
for i in field:
  for k,v in Counter(i).items():
    if k > 0 :
      dic[k] += v
# value 값 기준으로 오름차순 정렬
sorted_dict = dict(sorted(dic.items(), key=lambda x: x[1]))
for i in sorted_dict.values():
  print(i) #value 값 출력