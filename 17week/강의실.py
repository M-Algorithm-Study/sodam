# 백준 / 1374번 강의실(공통)

import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap, que = [], []

# 강의 시작과 종료시간 오름차순으로 리스트 만들기
for _ in range(n):
    num, start, end = map(int,input().split())
    heapq.heappush(heap, [start,end])

# 제일 먼저 시작하는 강의의 종료 시간 추가
heapq.heappush(que, heapq.heappop(heap)[1])

while heap:
    start, end = heapq.heappop(heap)
    # 가장 빠른 강의 종료 시간이 강의 시작시간 보다 빠르면 같은 강의실을 사용 할 수 있으므고
    if que[0] <= start:
        # 리스트에서 제외시키고 가장 빠른 종료시간 보다 시작시간이 빠르면 강의실이 추가로 필요해서 제외시키지 않는다.
        heapq.heappop(que)
    # 강의 종료 시간 추가
    heapq.heappush(que, end)

# 강의 종료 시간 갯수가 필요한 강의실의 개수 따라서 que 의 길이 출력
print(len(que))