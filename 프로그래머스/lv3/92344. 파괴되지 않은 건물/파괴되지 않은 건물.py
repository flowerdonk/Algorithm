def solution(board, skill):
    answer = 0
    M = len(board[0])
    N = len(board)
    
    add = [[0] * (M + 1) for _ in range(N + 1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        change = degree
        if type == 1:
            change = -degree
        add[r1][c1] += change
        add[r2 + 1][c2 + 1] += change
        add[r1][c2 + 1] -= change
        add[r2 + 1][c1] -= change
    
    for x in range(N):
        for y in range(M):
            add[x][y + 1] += add[x][y]
    
    for y in range(M):
        for x in range(N):
            add[x + 1][y] += add[x][y]
        
    for i in range(N):
        for j in range(M):
            board[i][j] += add[i][j]
            if board[i][j] > 0:
                answer += 1
        
    return answer