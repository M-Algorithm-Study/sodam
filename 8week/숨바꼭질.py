# 백준 / 1697번 숨바꼭질(공통)

from collections import deque

def bfs():
    queue = deque()
    # 출발점 추가
    queue.append(n)
    while queue:
        m = queue.popleft()
        # 위치가 동생 위치와 같으면 종료
        if m == k:
            print(visit[m])
            break
        # 이동 가능한 곳 안에서
        for i in (m-1,m+1,m*2):
            # 범위를 벗어 나지 않고 아직 방문하지 않았다면
            if 0 <= i <= cnt and not visit[i]:
                # 해당 위치에 현재 이동한 시간 추가
                visit[i] = visit[m] + 1
                # 해당 위치 리스트에 추가
                queue.append(i)
                
cnt = 10 ** 5 # 최대좌표
visit = [0] * (cnt + 1)
n, k = map(int,input().split())
bfs()