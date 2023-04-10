import sys
from collections import deque
sys.stdin = open('input.txt')

'''
N X N
물고기 1~6, 아기상어 9(처음 크기 2), 빈칸 0
자신의 크기와 같은 수의 물고기를 먹을 때마다 크기 1 증가
한 칸에 물고기 1마리 이하
1초에 상하좌우 한 칸씩 이동, 이동은 1초 소요
이동 가능 칸: 자신의 크기보다 큰 물고기가 있는 칸 제외 모두
먹을 수 있는 물고기: 자신의 크기보다 작은 물고기(같은 물고기 불가능)
1. 거리가 가장 가까운 물고기 2. 가장 위에 있는 물고기 3. 가장 왼쪽에 있는 물고기
'''
N = int(input())
data = [[7] * (N + 2)] + [[7] + list(map(int, input().split())) + [7] for _ in range(N)] + [[7] * (N + 2)]
size = 2
si, sj = 0, 0
for i in range(N + 2):
    for j in range(N + 2):
        if data[i][j] == 9:
            si, sj = i, j

q = deque()
q.append((si, sj, size))
while q:
    i, j, s = q.popleft()
    tlist = []
    for di, dj in (-1, 0), (0, 1), (1, 0), (0, -1):
        ti, tj = i, j
        ni, nj = ti + di, tj + dj # 이동한 위치
        temp = 1 # 이동한 거리
        flag = 0
        while data[ni][nj] != 7 and data[ni][nj] <= s:
            if 0 < data[ni][nj] < s:
                flag = 1
                break
            ni += di
            nj += dj
            temp += 1
        if flag == 1:
            tlist.append((ni, nj, temp)) # 도착한 위치, 거리
    print(tlist)