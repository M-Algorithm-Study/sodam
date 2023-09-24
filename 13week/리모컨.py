# 백준 / 1107번 리모컨(공통)

import sys
input = sys.stdin.readline

n=int(input())
m=int(input())
btn=abs(n-100)

if m == 0:
    print(min(btn,len(str(n)))) 
    sys.exit()
# 고장난 버튼이 0개일 경우 버튼이 눌리는 최소 값 출력하고 종료

else:
    lst=list(input().strip())
    
for i in range(1000001):
    i=str(i)
    chk=True
    # 채널 숫자 중 고장난 버튼이 있으면 false
    for j in range(len(i)):
        if i[j] in lst:
            chk=False
            break
        
    if chk==True: #고장난 버튼이 없으면 최소 값 재설정
        btn=min(btn, abs(n-int(i))+len(i))
print(btn)


