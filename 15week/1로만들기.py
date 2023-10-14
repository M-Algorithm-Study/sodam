# 백준 / 1463번 1로만들기(공통)

n = int(input())
cnt = [0] * (n+1)

# 1은 0번임으로 2부터 시작

for i in range(2,n+1):
    cnt[i] = cnt[i-1] + 1

# 빼는 것과 나누었을 때 나오는 횟수를 비교해서 작은 횟수로 업데이트
    if i % 2 == 0:
        cnt[i] = min(cnt[i], cnt[i//2]+1)
    if i % 3 == 0:
        cnt[i] = min(cnt[i], cnt[i//3]+1)

print(cnt[n])