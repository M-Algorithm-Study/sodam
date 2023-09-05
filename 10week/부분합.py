# 백준 / 1806번 부분합(공통)
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = list(map(int,input().split()))

# 최소 길이 비교 할 변수 셋팅
min = 100001
# 왼쪽포인터, 오른쪽 포인터
left,right = 0,1
# 합산
cnt = lst[left]

# 왼쪽 포인터가 리스트의 길이를 벗어나지 않을 동안만
while left < n:
  # 합산이 m 보다 크거나 같으면
  if cnt >= m:
    # 수열의 길이가 기존 최소 길이보다 짧으면
    if (right - left) < min:
      # 최소 길이 재설정
      min = (right - left)
    # 합산에서 왼쪽 포인터가 있는 수를 빼주고
    cnt -= lst[left]
    # 왼쪽 포인터 한칸 이동
    left += 1

  # 오른쪽 포인터가 리스트의 끝에 왔는데 합산이 m 보다 작으면
  if right == n and cnt < m:
    # 탈출
    break

  # 합산이 m보다 작으면
  if cnt < m:
    # 합산에 오른쪽 포인터의 수를 더해주고
    cnt += lst[right]
    # 오른쪽 포인터 한칸 이동
    right += 1

# 최소 길이가 100001에서 바뀌지 않았으면 합을 만드는 것이 불가능 하다는 의미로
if min == 100001:
  # 0 출력
  print('0')
  # 아니라면 최소 길이 출력
else:
  print(min)

