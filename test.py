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
def find_mn(lst, n):
    idx = 0
    for l in range(1, len(lst)):
        if lst[l][n] == lst[0][n]:
            mn_idx = l
        else:
            break
    return idx

N = int(input())
data = [[7] * (N + 2)] + [[7] + list(map(int, input().split())) + [7] for _ in range(N)] + [[7] * (N + 2)]
si, sj = 0, 0
size = 2
time = 0
for i in range(N + 2):
    for j in range(N + 2):
        if data[i][j] == 9:
            si, sj = i, j

q = deque()
q.append(((si, sj), 0))
while q:
    visited = [[0] * (N + 2) for _ in range(N + 2)]
    (i, j), s = q.popleft()
    if s == size:
        size += 1
    data[i][j] = 0

    tlist = []
    for di, dj in (-1, 0), (0, 1), (1, 0), (0, -1):
        ti, tj = i + di, j + dj
        ni, nj = ti, tj # 이동한 위치
        while data[ni][nj] != 7 and data[ni][nj] <= size and visited[ni][nj] == 0:
            temp = 1 # 이동한 거리
            flag = 0
            for ddi, ddj in (-1, 0), (0, 1), (1, 0), (0, -1):
                if di == ddi and dj == ddj:
                    continue
                while data[ni][nj] != 7 and data[ni][nj] <= size and visited[ni][nj] == 0:
                    if 0 < data[ni][nj] < size:
                        flag = 1
                        break
                    visited[ni][nj] = 1
                    ni += ddi
                    nj += ddj
                    temp += 1
                if flag == 1 and visited[ni][nj] == 0:
                    tlist.append((ni, nj, temp)) # 도착한 위치, 거리
                if data[ni][nj] != 7:
                    visited[ni][nj] = 1
                ni, nj = ti, tj
            ni += di
            nj += dj

    tlist.sort(key=lambda x:x[2])
    mn_idx = find_mn(tlist, 2)

    if mn_idx != 0:
        tlist.sort(key=lambda x:x[0])
        mn_idx = find_mn(tlist, 0)

        if mn_idx != 0:
            tlist.sort(key=lambda x:x[1])
            mn_idx = find_mn(tlist, 1)

    if tlist:
        q.append((tlist[mn_idx][:2], s + 1))
        time += tlist[mn_idx][2]
    else:
        break
    print(tlist)
print(time)
