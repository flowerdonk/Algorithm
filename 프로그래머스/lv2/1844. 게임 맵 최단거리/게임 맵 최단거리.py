# import sys
# sys.setrecursionlimit(10**9)

# def solution(maps):
#     answer = []
#     N = len(maps)
#     M = len(maps[0])
#     visited = [[10001] * M for _ in range(N)]
#     dfs((0, 0), maps, visited, answer, 0)

#     if answer:
#         return min(answer)
#     else:
#         return -1

# def dfs(start, maps, visited, answer, cnt):
#     N = len(maps)
#     M = len(maps[0])
#     i, j = start
#     visited[i][j] = cnt
    
#     if i == N - 1 and j == M - 1:
#         answer.append(cnt + 1)
    
#     for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
#         ni, nj = i + di, j + dj
#         if 0 <= ni < N and 0 <= nj < M and maps[ni][nj] == 1 and visited[ni][nj] >= cnt:
#             dfs((ni, nj), maps, visited, answer, cnt + 1)

from collections import deque
def solution(maps):
    answer = 0
    
    N = len(maps)
    M = len(maps[0])
    visited = [[0] * M for _ in range(N)]
    
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    
    while q:
        i, j = q.popleft()
        if i == N - 1 and j == M - 1:
            answer = visited[i][j]
        
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and maps[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
        
    if answer:
        return answer
    else:
        return -1