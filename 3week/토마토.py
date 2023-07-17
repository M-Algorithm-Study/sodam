# 백준 / 7569번 토마토(공통)

import sys
from collections import deque
input = sys.stdin.readline
# 가로세로높이
M,N,H = map(int,input().split())

#3차원 토마토 상자
tomatoes = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
# 인접한 토마토 체크
tomato = deque()

#좌우상하고저 확인
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

#토마토가 익은 상태면 리스트에 추가
for i in range(H):
    for j in range(N):
        for k in range(M):
            if(tomatoes[i][j][k] == 1):
                tomato.append([i,j,k])

#인접한 토마토에 +1 일씩 더 한 날짜로 갱신
while tomato:
        z,x,y = tomato.popleft()

        for i in range(6):
            nx,ny,nz = x + dx[i], y + dy[i], z + dz[i]
            
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
                if tomatoes[nz][nx][ny] == 0:
                    tomatoes[nz][nx][ny] = tomatoes[z][x][y] + 1
                    tomato.append([nz,nx,ny])
                    
cnt = 1
result = -1

# 상자를 순회하면서 
for i in tomatoes:
    for j in i:
        for k in j:
            # 안익은 토마토가 있으면 체크
            if k == 0:
                cnt = 0
            # 가장 큰 날짜로 갱신
            result = max(result,k)
if(cnt == 0):
    print(-1)
elif(result == 1):
    print(0)
else:
    print(result -1)
