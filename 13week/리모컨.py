# 백준 / 1107번 리모컨(공통)

import sys
input = sys.stdin.readline

n,m = int(input()), int(input())
lst = list(input().strip())
btn = abs(n-100)

if m == 0:
  print(min(btn, len(str(n)))) 
# 고장난 버튼이 0개일 경우 버튼이 눌리는 최솟값 출력
else: 
# 완전탐색 (주어지는 제일 큰 채널 500,000 기준 최댓값 999,901까지 탐색)
  for i in range(999901):
    i = str(i)
    chk = 1
    # 채널 숫자 중 고장난 버튼이 있으면 false
    for j in i:
      if j in lst:
        chk = 0
        break
        
    if chk: #고장난 버튼이 없으면 최솟값 재설정
      btn = min(btn, abs(n-int(i))+len(i))
  print(btn)


