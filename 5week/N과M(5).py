# 백준 / 15654번 N과 M(5)

from itertools import permutations
n,m= map(int,input().split())
num = sorted(list(map(int,input().split())))

for i in permutations(num,m):
    print(*i)


# [멀티잇] 코딩테스트 러닝클래스'Python 7월반 4회 완전탐색 수 이어 붙이기 문제에서 배운 라이브러리