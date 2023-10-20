# 백준 / 14888번 연산자끼워넣기(공통)

def dfs(result, num):
    global max_num,min_num
    if num == n:
        # 최댓값과 최솟값 설정하고 함수 종료
        min_num = min(min_num, result)
        max_num = max(max_num, result)
        return 
    
    for i in range(4) :
        temp = 0

        # 연산자 개수가 0 이면 pass
        if cal[i] == 0: 
            continue
        
        if i == 0: 
            temp = result + lst[num]

        if i == 1: 
            temp = result - lst[num]

        if i == 2: 
            temp = result * lst[num]

        # 음수일 경우 양수로 바꾸고 몫을 음수로 바꾸기
        if i == 3: 
            if result < 0: 
                temp = -(-result // lst[num])
            else: 
                temp = result // lst[num]
        # 연산자 개수 하나 줄이기
        cal[i] -= 1
        dfs(temp, num+1)
        # 함수가 끝난 후 연산자 수 복구
        cal[i] += 1


n = int(input())
lst = list(map(int, input().split()))
cal =  list(map(int, input().split()))
max_num = -1000000001
min_num =  1000000001

dfs(lst[0], 1)
print(max_num)
print(min_num)
