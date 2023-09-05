# 백준 / 2583번 영역구하기(공통)

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

m,n,k = map(int, input().split())

field = [[0] * n for _ in range(m)] 

# 모눈종이에 직사각형 구역 표시하기
for _ in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            field[y][x] = 1

# 모눈종이에 비어있는 공간 체크하고 연결 된 구역 카운트
def dfs(x, y, cnt):
    field[y][x] = 1
    for d in direct:
        dx, dy = x + d[0], y + d[1]
        if (0 <= dx < n) and (0 <= dy < m) and field[dy][dx] == 0:
            cnt = dfs(dx, dy, cnt+1)
    return cnt

# 분리된 영역 넓이 쌓아줄 빈 리스트
area = []
direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 리스트에 분리된 영역의 넓이 쌓아주기
for y in range(m):
    for x in range(n):
        if field[y][x] == 0:
            area.append(dfs(x, y, 1))

# 리스트 길이 출력(분리된 영역의 개수)
print(len(area))
# 리스트 정렬 출력(오름차순으로 영역의 넓이 출력)
print(*sorted(area))