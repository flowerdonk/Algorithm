def Bus(N, lineA, P, lineN):
    count = [0] * 5001
    result = []
    for i in range(N):
        for j in range(lineA[i][0] - 1, lineA[i][1]):
            count[j] += 1

    # 주어진 정류장 번호에 지나는 버스 노선 개수
    for i in range(P):
        result.append(count[lineN[i] - 1])
    return result

T = int(input())
result = []
for i in range(T):
    N = int(input())
    lineA = []
    for i in range(N):
        lineA.append(list(map(int, input().split())))
    P = int(input())
    lineN = []
    for i in range(P):
        lineN.append(int(input()))
    result.append(Bus(N, lineA, P, lineN))

for i in range(T):
    print(f'#{i + 1}', *result[i])

