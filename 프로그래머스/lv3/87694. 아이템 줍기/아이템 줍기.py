from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    boardy = max(rectangle, key=lambda x:x[3])[3] * 2 + 2
    boardx = max(rectangle,key=lambda x:x[2])[2] * 2 + 2
    board = [[-1] * (boardy) for _ in range(boardx)]
    
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x : x*2, rec)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if x1 < x < x2 and y1 < y < y2:
                    board[x][y] = 0
                elif board[x][y] != 0:
                    board[x][y] = 1 
    
    q = deque()
    q.append((characterX * 2, characterY * 2))
    visited = [[1] * boardy for _ in range(boardx)]

    while q:
        x, y = q.popleft()
        
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break
        
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < boardx and 0 <= ny < boardy:
                if board[nx][ny] == 1 and visited[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    return answer