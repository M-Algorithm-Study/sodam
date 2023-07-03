# 백준 / 11729번 하노이 탑 이동순서 (공통)

def hanoi(n,s,m,e):
    # 원반 1개면 시작, 끝 출력하고 종료
    if n == 1:
        print(s,e)
        return
    
    hanoi(n-1,s,e,m)
    print(s,e)
    hanoi(n-1,m,s,e)

n = int(input())
print(2**n-1)
hanoi(n,1,2,3)


#메모리: 31256 KB, 시간: 884 ms, 코드길이 179B