import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    data = [input() for _ in range(5)]
    result = ''
    mx_len = len(max(data, key = lambda x : len(x)))

    for j in range(mx_len): # 가로
        for i in range(5): # 세로
            if j <= len(data[i]) - 1:
                result += data[i][j]
            else:
                continue

    print(f'#{tc} {result}')