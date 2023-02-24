def Sub(Test_N, N, Test):
    subs = []

    for i in range(Test_N):
        max = 0
        min = 1000001
        for case in Test[i]:
            if max <= case:
                max = case
            if min >= case:
                min = case

        subs.append(max - min)
    return subs

Test_N = int(input())
N = []
Test = []
for i in range(Test_N):
    N.append(int(input()))
    Test.append(list(map(int, input().split())))

for i in range(Test_N):
    print(f'#{i + 1} {Sub(Test_N, N, Test)[i]}')