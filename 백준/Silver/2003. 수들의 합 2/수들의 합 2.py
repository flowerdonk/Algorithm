N, M = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 1
total = arr[0]
cnt = 0

while right <= N and left <= right:
    if total == M:
       cnt += 1
       total -= arr[left]
       left += 1
    elif total < M:
        if right == N:
            break
        total += arr[right]
        right += 1
    else:
        total -= arr[left]
        left += 1

print(cnt)