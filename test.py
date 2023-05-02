import sys
sys.stdin = open('input.txt')

n = int(input())
bambu = [list(map(int, input().split())) for _ in range(n)]
# ans: 해당 지점을 시작점으로 이동한 최대 칸 저장
ans = [[0] * n for _ in range(n)]

'''
[1] 특정 지점에서 dfs
이동 가능한 지점에 ans 값이 있을 경우, 생략 -> DP
'''
def dfs(si, sj):
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    stack = [(si, sj, 0)]
    # 방문 표시
    visited = [[0] * n for _ in range(n)]

    # 가는 곳 stack에 저장, 후입선출
    while stack:
        # 현재 좌표, 이동 칸 수
        i, j, cnt = stack.pop()
        # 이동할 수 없는 지점까지 갔을 때, 해당 칸까지의 cnt 저장, 나중에 최댓값 찾기
        mxs = []
        # 시계방향으로 돌며 확인, ans에 값이 있으면 continue
        for di, dj in direction:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
                if bambu[ni][nj] > bambu[i][j]:
                    # 이미 계산한 지점일 경우, 지금까지의 이동 칸 수 + 저장된 값
                    if ans[ni][nj] != 0:
                        mxs.append(cnt + ans[ni][nj])
                        continue
                    else:
                        i = ni
                        j = nj
                        visited[i][j] = 1
                        stack.append((i, j, cnt + 1))
                else:
                    mxs.append(cnt)

dfs(0, 0)
print(ans)