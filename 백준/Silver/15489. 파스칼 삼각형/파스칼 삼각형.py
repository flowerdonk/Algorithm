from sys import stdin

R, C, W = map(int, stdin.readline().split())
pascal = [[0] * n for n in range(1, R + W + 1)]

pascal[0][0] = 1
pascal[1][0], pascal[1][1] = 1, 1

for n in range(1, R + W - 1):
    pascal[n + 1][0] = 1
    pascal[n + 1][n + 1] = 1
    for m in range(n):
        pascal[n + 1][m + 1] = pascal[n][m] + pascal[n][m + 1]

ans = 0
for i in range(W):
    for j in range(i + 1):
        ans += pascal[R + i - 1][C + j - 1]
print(ans)