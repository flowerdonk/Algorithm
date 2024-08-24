N, M = map(int, input().split())
tree = list(map(int, input().split()))

left, right = 1, max(tree)
mid = 0

while left <= right:
    mid = (left + right) // 2
    total = sum((tree[i] - mid for i in range(N) if tree[i] > mid))
    if total >= M:
        left = mid + 1
    elif total < M:
        right = mid - 1

print(right)