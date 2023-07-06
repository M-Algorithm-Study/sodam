# 백준 / 10799번 쇠막대기 (공통)

n = input()
stick = n.replace('()','|')
# 잘리는 부분을 word 1개로 변환
cnt, result = 0, 0

for i in stick:
    # 열리는 괄호면 막대 갯수 추가
    if i == '(':
        cnt += 1
    # 닫히는 괄호면 막대 갯수 감소, 잘린 막대 꽁지 +1
    elif i == ')':
        cnt -= 1
        result += 1
    # 절단 시, 카운트 된 막대 갯수 만큼 +
    else:
        result += cnt

print(result)

# 메모리 31388KB/ 시간 56 ms/ 코드길이 211B