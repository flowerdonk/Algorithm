import sys
sys.stdin = open('input.txt')

def pizza(N, M, arr):
    ans = 0
    Narr = list(enumerate(arr)) # (인덱스, 값) 형식으로 리스트화
    fire = [] # 화덕에 들어가는 피자들

    for n in range(N): # 지정된 N개 만큼 팝, 어펜드
        fire.append(Narr.pop(0))

    while fire: # 화덕이 빌 때 까지
        for n in range(N): # 한 사이클 -> 화덕에 들어가는 피자 수 N
            if len(fire) == 1: # 화덕에 하나밖에 없을 때
                ans = fire[0][0] # 해당 인덱스 변수 할당
                fire.pop() # 화덕 비움
                break # 반복문 종료

            fst = fire.pop(0) # 맨 앞 값 변수 할당

            if fst[1] == 0: # 치즈가 다 녹았을 때
                if Narr: # 아직 화덕에 안들어간 피자가 있다면
                    add = Narr.pop(0) # 들어가야할 피자 정보 변수 할당
                    fire.append((add[0], add[1] // 2)) # (인덱스, 값 //2) 삽입
                continue # 반복문 건너뛰기

            fire.append((fst[0], fst[1] // 2)) # (인덱스, 값 //2) 삽입

    return (ans + 1) # 인덱스가 0부터 시작하기 때문에 + 1

T = int(input())
for i in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{i} {pizza(N, M, arr)}')