import sys
sys.stdin = open('input.txt')

def turn(N, M, arr):
    for n in range(M): # 지정된 회전 수 만큼 반복
        fst = arr.pop(0) # 맨 앞 값 변수 할당
        arr.append(fst) # 맨 뒤에 삽입

T = int(input())
for i in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    turn(N, M, arr)

    print(f'#{i} {arr[0]}')