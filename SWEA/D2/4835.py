def Sub(T, N, Test):
    subs = []
    for i in range(T):
        max = 0
        min = 10000000
        for j in range(N[i][0] - N[i][1] + 1): 
            # i번째 케이스의 정수 개수 - 구간 수 + 1 까지
            sum = 0
            for k in range(N[i][1]):
                sum += Test[i][j + k]

            if sum >= max:
                max = sum
            if sum <= min:
                min = sum

        subs.append(max - min)

    return subs


T = int(input())
N = []
Test = []
for i in range(T):
    N.append(list(map(int, input().split())))
    Test.append(list(map(int, input().split())))

for i in range(T):
    print(f'#{i + 1} {Sub(T, N, Test)[i]}')