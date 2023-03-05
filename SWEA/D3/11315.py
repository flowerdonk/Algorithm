import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [input() for _ in range(N)]
    result = 0
    direction = [[0, 1], [1, 0], [1, 1], [1, -1]] # 오른쪽, 아래, 오른쪽 아래 대각선, 왼쪽 아래 대각선

    for i in range(len(data)): # 입력 데이터에서 돌 위치 파악
        if result >= 1: # 5개 연속이 하나라도 있으면 반복문 벗어나기
            break
        for j in range(len(data[i])):
            if data[i][j] == 'o': # 돌을 찾으면 그 위치가 시작점
                for d in direction: # 방향 하나씩 확인
                    cnt = 1 # 바둑 개수
                    ni = i + d[0] # 해당 방향으로 이동한 위치
                    nj = j + d[1]
                    while 0 <= ni < N and 0 <= nj < N and data[ni][nj] == 'o':
                        cnt += 1
                        ni += d[0]
                        nj += d[1]

                    if cnt >= 5:
                        result += 1

    print(f'#{tc} ', end = '')
    if result >= 1:
        print('YES')
    else:
        print('NO')

