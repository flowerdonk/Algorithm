N, K = map(int, input().split())
data = list(map(int, input().split()))

total = sum(data[:K])
mx = total
for n in range(1, N - K + 1):
    l = data[n - 1]
    r = data[n + K - 1]
    total = total - l + r
    if mx <= total:
        mx = total

print(mx)
