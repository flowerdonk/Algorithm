# 교수님 풀이
T = int(input())

memo = [[0 for _ in range(11)] for _ in range(11)]

for i in range(10):
    for j in range(i + 1):
        if j == 0 or i == j:
            memo[i][j] = 1
        else:
            memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]

for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')

    for i in range(N):
        for j in range(i + 1):
            print(f'{memo[i][j]}', end = ' ')
        print()


# 직접 풀이
def pascal(N):
    memo = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(i + 1):
            if j == 0 or j == i:
                memo[i][j] = 1
            else:
                memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]
    return memo

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    ans = pascal(N)

    print(f'#{i}')
    for n in range(N):
        for m in range(n + 1):
            print(f'{ans[n][m]}', end = ' ')
        print()