import sys
sys.stdin = open('input.txt')
'''
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input()))
    ans = cnt = 0

    for i in range(N):
        if lst[i] == 0:
            cnt = 0

        else:
            cnt += 1
            if ans < cnt:
                ans = cnt

    print(f'#{test_case}', ans)
'''
def MaxTimes(N, Seque):
    times = 0
    max = 0
    for i in range(N):
        if Seque[i] == 1:
            times += 1
            if max <= times:
                max = times
        else:
            times = 0

    return max

T = int(input())
N = []
Seque = []

for i in range(T):
    N.append(int(input()))
    Seque.append(list(map(int, list(input()))))

for i in range(T):
    print(f'#{i + 1} {MaxTimes(N[i], Seque[i])}')