def Fly(Detail):
    D = Detail[0]
    A = Detail[1]
    B = Detail[2]
    F = Detail[3]
    last = D / (A + B)
    return last * F


T = int(input())
Result = []
for i in range(T):
    Detail = list(map(int, input().split()))
    Result.append(Fly(Detail))

for i in range(T):
    print(f'#{i + 1} {Result[i]}')
