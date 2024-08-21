X, Y = map(int, input().split())
mid = Y * 100 // X
right = mid + 1
N = mid * X + X - 100 * Y
D = 99 - mid
print(-1 if mid >= 99 else N // D + (N % D > 0))