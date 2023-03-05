import sys
sys.stdin = open('input.txt')

def subset(A):
    total = []
    for i in range(1 << len(A)):
        subs = []
        for j in range(len(A)):
            if i & (1 << j):
                subs.append(A[j])
        total.append(subs)
            
    return total

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())
result = [0] * T

for i in range(T):
    N, K = map(int, input().split())
    all = subset(A)

    for sub in all:
        if len(sub) == N and sum(sub) == K:
            result[i] += 1

for i in range(T):
    print(f'#{i + 1} {result[i]}')