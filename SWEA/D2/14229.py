def msort(s, e):
    if s == e:
        return
    m = (s + e) // 2
    msort(s, m)
    msort(m + 1, e)

    k = 0
    l, r = s, m + 1  # 왼쪽과 오른쪽에서 가장 작은 숫자의 위치

    while l <= m or r <= e:
        if l <= m and r <= e:
            if arr[l] <= arr[r]:
                temp[k] = arr[l]
                l += 1
            else:
                temp[k] = arr[r]
                r += 1
            k += 1
        elif l <= m:  # l이 남아있는 상태라면
            while l <= m:
                temp[k] = arr[l]
                l += 1
                k += 1
        elif r <= e:  # r이 남아있는 상태라면
            while r <= e:
                temp[k] = arr[r]
                r += 1
                k += 1

    i = 0
    while i < k:
        arr[s + i] = temp[i]
        i += 1

    return


N = 1000000
arr = list(map(int, input().split()))
temp = [0] * N  # 합칠 때 임시 저장하는 용도
msort(0, N - 1)
print(arr[500000])