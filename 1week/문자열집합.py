# 백준 / 14425 문자열 집합
# 제출

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = [input().strip() for _ in range(n)]
lst2 = [input().strip() for _ in range(m)]
cnt = 0

for i in lst2:
    if i in lst:
        cnt += 1
print(cnt)

# 메모리 41936 KB/ 시간 3732 ms/ 코드길이 223 B