# 백준 / 20920번 영단어암기는 괴로워 (공통)

import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
word = {}

for _ in range(n):
    a = input().strip()
    if len(a) >= m:
        if a in word:
            word[a] += 1
        else:
            word[a] = 1

# 자주 나오는 횟수, 단어 길이, 사전순 정렬
word = sorted(word.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in word:
    print(i[0])