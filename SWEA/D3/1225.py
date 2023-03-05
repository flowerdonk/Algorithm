import sys
sys.stdin = open('input.txt')

def code(arr):
    cnt = 1

    while cnt: # 0 이하 발생 시 반복문 종료
        for n in range(1, 6): # 5씩 싸이클
            fst = arr.pop(0) # 맨 앞 변수에 할당

            if fst - n <= 0: # 감소한 수가 0 이하일 때
                arr.append(0) # 0 삽입
                cnt = 0 # 반복문 종료
                break

            else:
                arr.append(fst - n) # 감소한 수 삽입

T = 10
for i in range(1, T + 1):
    _ = input()
    arr = list(map(int, input().split()))
    code(arr)
    
    print(f'#{i}', *arr)


## 교수님 풀이
for _ in range(10):
    tc = int(input())
    data = list(map(int, input().split())) # 받은 input 자체를 큐로 활용
    # 현재 싸이클에서 감소시켜줘야하는 값
    cnt = 1

    while data[-1] > 0:
        if cnt > 5:
            cnt = 1

        # 첫번째 위치한 숫자를 감소시킨 뒤 맨 뒤로 보내기
        data.append(data.pop(0) - cnt)
        cnt += 1

    # 데이터의 마지막 값은 0으로 고정정
    data[-1] = 0