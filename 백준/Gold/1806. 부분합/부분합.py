N, S = map(int, input().split())
arr = list(map(int, input().split()))

arr_sum = [arr[0]]

# 누적합
for n in range(1, N):
    arr_sum.append(arr_sum[n - 1] + arr[n])

min_len = 999999

left, right = -1, 0

while left <= right and right < N:
    if left == -1:
        diff = arr_sum[right]
    else:
        diff = arr_sum[right] - arr_sum[left]

    if diff >= S:
        min_len = min(min_len, right - left)
        left += 1
    else:
        right += 1

print(min_len if min_len != 999999 else 0)