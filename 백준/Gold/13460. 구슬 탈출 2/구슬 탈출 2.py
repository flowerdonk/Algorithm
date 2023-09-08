from collections import deque

N, M = map(int, input().split())
board = []
rx, ry, bx, by = 0, 0, 0, 0
for n in range(N):
    line = list(input())
    board.append(line)
    for m in range(M):
        if line[m] == 'R':
            rx, ry = n, m
        elif line[m] == 'B':
            bx, by = n, m

# 시계방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def move(x, y, dir):
    nx, ny = x, y
    
    while True:
        nx += dx[dir]
        ny += dy[dir]
        
        if board[nx][ny] == '#':
            nx -= dx[dir]
            ny -= dy[dir]
            break
            
        if board[nx][ny] == 'O':
            break
            
    return nx, ny

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by))
    visited = []
    visited.append((rx, ry, bx, by))
    cnt = 0

    while q:
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()

            if cnt > 10:
                return -1

            if board[rx][ry] == 'O':
                return cnt

            for dir in range(4):
                nrx, nry = move(rx, ry, dir)
                nbx, nby = move(bx, by, dir)
                if board[nbx][nby] == 'O':
                    continue
                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dx[dir]
                        nry -= dy[dir]
                    else:
                        nbx -= dx[dir]
                        nby -= dy[dir]
                if (nrx, nry, nbx, nby) not in visited:
                    q.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
                    
        cnt += 1
        
    return -1

print(bfs(rx, ry, bx, by))