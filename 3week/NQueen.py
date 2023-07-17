# 백준 / 9663번 N-Queen(공통)

# import sys
# input = sys.stdin.readline
# n = int(input())

# field = [[0]*n for i in range(n)]
# cnt = 0

# def queen(x):
    
#     if x == n:
#         global cnt
#         cnt+=1
#         return
    
#     for i in range(n):
#       skip = 0
#       for j in range(n):
#         if field[j][i] == 1:
#             break
#       else:
#         for k in range(x):
#           if (field[k].index(1) == i + x - k) or (field[k].index(1) == i - (x - k)):
#               skip = 1
#               break
#         if skip == 1:
#             continue
#         field[x][i] = 1
#         queen(x+1)
#         field[x][i] = 0
# queen(0)
# print(cnt)

import sys
n, cnt = int(sys.stdin.readline()), 0
a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)

def solve_dfs(i):
    global cnt
    if i == n:
        cnt += 1
        return
    for j in range(n):
        if (not a[j] and not b[i+j] and not c[i-j+n-1]) :
            a[j] = b[i+j] = c[i-j+n-1] = True
            solve_dfs(i+1)
            a[j] = b[i+j] = c[i-j+n-1] = False

solve_dfs(0)
print(cnt)


# 모르겠어여 ...... 
# 어케 해야 되는 건지, 백트래킹 이해는 했는데 코드를 이해 못하겠어여 ... 