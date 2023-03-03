def Card(N, A_list, B_list):
    result = []

    for i in range(N):
        num_A = A_list[i][0]
        num_B = B_list[i][0]

        # 0 - 세모, 1 - 네모, 2 - 동그라미, 3 - 별
        shape_A = [0] * 4
        shape_B = [0] * 4
        for r in range(1, num_A + 1):
            shape_A[A_list[i][r] - 1] += 1
        for r in range(1, num_B + 1):
            shape_B[B_list[i][r] - 1] += 1

        for i in range(3, -1, -1): # 그림 비교 별 -> 세모
            if shape_A[i] > shape_B[i]:
                result.append('A')
                break
            elif shape_A[i] < shape_B[i]:
                result.append('B')
                break
            else:
                if i != 0:
                    continue
                else:
                    result.append('D')
                    break

    return result


N = int(input())
A_list = []
B_list = []

for i in range(N):
    A_list.append(list(map(int, input().split())))
    B_list.append(list(map(int, input().split())))

result = Card(N, A_list, B_list)
for i in range(N):
    print(result[i])
