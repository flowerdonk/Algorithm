import sys
sys.stdin = open('sample_in.txt')

def NewBus(N, Detail):
    # station = [0] * 1001
    result = []

    for i in range(N):
        result.append(Detail[i][1])
        result.append(Detail[i][2])

        if Detail[i][0] == 1: # 일반 버스, 모든 정류장 정차
            for j in range(Detail[i][1] + 1, Detail[i][2]):
                result.append(j)

        elif Detail[i][0] == 2: # 급행 버스, 짝수끼리, 홀수끼리
                for j in range(Detail[i][1] + 2, Detail[i][2], 2):
                    result.append(j)

        elif Detail[i][0] == 3: # 광역 버스, 짝수-4의 배수, 홀수-3의 배수 & 10의 배수 X
            if Detail[i][1] % 2: # 홀수

                for j in range(Detail[i][1] + 1, Detail[i][2]):
                    if not (j % 3) and (j % 10):
                        result.append(j)

            else: # 짝수
                for j in range(Detail[i][1] + 1, Detail[i][2]):
                    if not j % 4:
                        result.append(j)
    result.sort()
    count = [0] * (max(result) + 1)

    for i in result:
        count[i] += 1

    return max(count)

T = int(input())
Ns = []
Details = []
Detail = []
for i in range(T):
    Ns.append(int(input()))
    for i in range(Ns[i]):
        Detail.append(list(map(int, input().split())))
    Details.append(list(Detail))

for i in range(T):
    print(f'#{i + 1} {NewBus(Ns[i], Details[i])}')