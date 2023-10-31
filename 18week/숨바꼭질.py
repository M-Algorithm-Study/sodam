# 백준 / 13549번 숨바꼭질3(공통)

import sys
import heapq
input = sys.stdin.readline

n,m = map(int,input().split())
visit = [0]*100001
visit[n] = 1
# 최소시간을 출력하기 위해 heapq 사용
queue = [([0,n])]

while queue:
    # 수빈이가 동생 위치와 같아지면 시간 출력
    time,site = heapq.heappop(queue)
    if site == m:
        print(time)
        break
    
    # 순간이동의 경우
    tel = site * 2
    # 방문하지 않은 위치이고 범위 내면
    if tel < len(visit) and not visit[tel]:
        # 방문처리 후 리스트에 시간과 위치 추가 순간이동은 +0초
        visit[tel] = 1
        heapq.heappush(queue,(time,tel))
    
    # 한칸 앞으로 가거나 뒤로 가는 경우
    for i in (site+1, site-1):
        # 방문하지 않은 위치이고 범위 내면
        if i >= 0 and i < len(visit) and not visit[i]:
            # 방문 처리 후 시간,위치 추가 시간 +1초
            visit[i] = 1
            heapq.heappush(queue,(time+1,i))