import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
bambu = [list(map(int, input().split())) for _ in range(n)]
# dp: 해당 지점을 시작점으로 이동한 최대 칸 저장
dp = [[0] * n for _ in range(n)]

'''
[1] 특정 지점에서 dfs
이동 가능한 지점에 dp 값이 있을 경우, 생략 -> DP
'''
def dfs(si, sj):
    # dp에 값이 있으면 이미 이동 가능한 최대 칸이 저장된 지점 -> 값 바로 리턴
    if dp[si][sj]:
        return dp[si][sj]

    # 첫 시작점 1
    dp[si][sj] = 1

    # 시계방향으로 돌며 확인, 계속해서 재귀 호출
    for di, dj in direction:
        ni = si + di
        nj = sj + dj
        # 이동할 좌표가 범위 내, 또한 이전 좌표보다 대나무 수가 많을 경우
        if 0 <= ni < n and 0 <= nj < n and bambu[ni][nj] > bambu[si][sj]:
            # dp 값 갱신 -> dfs로 다시 들어감
            dp[si][sj] = max(dp[si][sj], dfs(ni, nj) + 1)

    return dp[si][sj]

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))

print(ans)