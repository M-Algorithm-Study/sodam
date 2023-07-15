# 백준 / 1904번 01타일

import sys
input = sys.stdin.readline

n = int(input())
a,b = 1, 2
cnt = 1 if n == 1 else 2

for i in range(3, n+1):
    cnt = (a + b) % 15746
    a, b = b, cnt
print(cnt)


#메모리: 31256 KB, 시간: 248 ms, 코드길이 171B