import sys
sys.stdin = open('input.txt')

def Carrot(N, C):
    times = 0
    max = 1
    for i in range(N - 1):
        if C[i] < C[i + 1]:
            times += 1
            if max <= times:
                max = times
        else:
            if times >= 1:
                max += 1
                times = 0

    if C[len(C) - 1] > C[len(C) - 2]:
        times += 1
        if max <= times:
            max = times
            
    return max


T = int(input())
N = []
C = []
for i in range(T):
    N.append(int(input()))
    C.append(list(map(int, input().split())))

for i in range(T):
    print(f'#{i + 1} {Carrot(N[i], C[i])}')