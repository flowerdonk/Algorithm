import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    N = int(input()) # 테이블 한 변 길이
    table_input = [list(input().split()) for _ in range(N)]
    table = list(zip(*table_input))
    cnt = 0
    # N : 1, 오른쪽으로 이동 / S : 2, 왼쪽으로 이동
    for i in range(N):
        stack = []
        for j in range(N):
            if table[i][j] == '1':
                stack.append('1')
            elif table[i][j] == '2':
                if stack and stack[-1] == '1':
                    cnt += 1
                    stack.clear()

    print(f'#{tc} {cnt}')