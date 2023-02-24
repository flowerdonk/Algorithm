import sys
sys.stdin = open('input.txt')
# 줄 단위로 입력, 한 줄씩 중복 없이 받아올 수 있음, 공백 포함

def View(T, N, Test):
    viewN = []

    for i in range(T):
        count = 0
        for r in range(2, N[i] - 2):
            group = [Test[i][r - 2], Test[i][r - 1], Test[i][r + 1], Test[i][r + 2]]
            if max(group) < Test[i][r]:
                count += Test[i][r] - max(group)

        viewN.append(count) 

    return viewN

T = 10
Test = []
N = []

for i in range(T):
    N.append(int(input()))
    Test.append(list(map(int, input().split())))

for i in range(T):
    print(f'#{i + 1} {View(T, N, Test)[i]}')
