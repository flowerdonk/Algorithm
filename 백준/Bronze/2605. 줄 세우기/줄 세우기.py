N = int(input())
data = list(map(int, input().split()))
std = [x for x in range(1, N + 1)]

for n in range(1, N):
    for l in range(data[n]):
        std[n - l - 1], std[n - l] = std[n - l], std[n - l - 1]

print(*std)