N = int(input())
arr = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))
arr.sort()

for target in targets:
    left, right = 0, N - 1
    temp = 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            temp = 1
            break
        elif arr[mid] < target:
            left = mid + 1
            continue
        else:
            right = mid - 1
            continue
    print(temp)