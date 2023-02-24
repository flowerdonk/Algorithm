def paper(N):
    arr = [1, 3]

    for i in range(2, N // 10):
        arr.append(arr[i - 2] * 2 + arr[i - 1])

    return arr[-1]

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    print(f'#{i} {paper(N)}')