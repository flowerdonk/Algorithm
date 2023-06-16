import sys
sys.setrecursionlimit(int(1e7))

def solution(maps):
    answer = []
    ilen = len(maps)
    jlen = len(maps[0])
    visited = [[0] * jlen for _ in range(ilen)]

    def dfs(i, j, total):
        visited[i][j] = 1
        total += int(maps[i][j])
        # 시작점에서 4방향
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < ilen and 0 <= nj < jlen and maps[ni][nj] != 'X' and visited[ni][nj] == 0:
                total = dfs(ni, nj, total)
        return total

    # 시작점
    for i in range(ilen):
        for j in range(jlen):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                tmp = dfs(i, j, 0)
                if tmp > 0:
                    answer.append(tmp)

    if not answer:
        return [-1]
    else:
        answer.sort()
        return answer