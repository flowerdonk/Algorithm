import sys
# from collections import deque
sys.stdin = open('input.txt')

# 0 : 빈칸, 1 : 벽, 2 : 바이러스
N, M = map(int, input().split())
v = []

data = []
cnt = 0
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 상, 우, 하, 좌
for n in range(N):
    l = list(map(int, sys.stdin.readline().rstrip().split()))
    for m in range(N):
        if l[m] == 2:
            v.append([n, m])
    data.append(l)


