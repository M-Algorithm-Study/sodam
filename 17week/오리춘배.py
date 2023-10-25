# 백준 / 30404번 오리와 박수치는 춘배

import sys
input = sys.stdin.readline

def duck():
    n, k = map(int,input().split())
    time = list(map(int,input().split()))
    cnt,claps = 0, 0

    for i in time:
        if cnt < i:
            cnt = i + k
            claps += 1
    print(claps)
duck()

