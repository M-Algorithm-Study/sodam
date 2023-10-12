# 백준 / 2747번 피보나치수(공통)

import sys
input = sys.stdin.readline

# def fi(n):
#   if n == 1 or n == 2:
#     return 1
#   elif n <= 0:
#     return 0
#   else:
#     return fi(n-1) + fi(n-2)

# print(fi(int(input())))

# 재귀 (시간초과)

n = int(input())
lst = [0, 1]

if n == 1 or n == 2:
  print(1)
else:
  for i in range(n-1):
    lst.append(lst[i]+lst[i+1])
  print(lst[-1])

# 3번째 수 부터 앞에 두 숫자를 더 한 값으로
# 더한 값을 리스트에 추가하고 마지막 숫자 출력
