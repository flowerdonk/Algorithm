import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    _ = input()
    data = [list(map(int, input().split())) for _ in range(100)]
    result = [0] * 202

    for i in range(100):
        for j in range(100):
            if i == j:
                result[200] += data[i][j]
            if i + j == 4:
                result[201] += data[i][j]

            result[i] += data[i][j]
            result[j + 100] += data[i][j]

    print(f'#{tc} {max(result)}')