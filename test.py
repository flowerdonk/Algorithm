import sys
sys.stdin = open('input.txt')

M, N, H = map(int, input().split()) # 가로, 세로, 높이
data = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
ans = -1
# 상, 우, 하, 좌, 앞, 뒤 [H, N, M]
direction = [[0, -1, 0], [0, 0, 1], [0, 1, 0], [0, 0, -1], [-1, 0, 0], [1, 0, 0]]

q = []
cnt0 = 0
visited = [[[0] * M for _ in range(N)] for _ in range(H)] # 익는 턴 저장
for h in range(H):
    for n in range(N):
        for m in range(M):
            if data[h][n][m] == 1: # 익은 사과
                q.append((h, n, m)) # 스택에 추가 -> 시작점
                visited[h][n][m] += 1 # 시작점 표시
            elif data[h][n][m] == 0: # 안익은 사과 갯수 추가
                cnt0 += 1

if cnt0 == 0: # 안익은 사과가 없으면 바로 종료
    q.clear()
    ans = 1

while q:
    sh, sn, sm = q.pop(0)
    data[sh][sn][sm] = 1 # 익음

    for d in direction:
        nh, nn, nm = sh + d[0], sn + d[1], sm + d[2] # 이동할 좌표
        if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M: # 범위 내
            if data[nh][nn][nm] == 0: # 안 익은 사과
                if visited[nh][nn][nm] == 0: # 방문한 적 X
                    q.append((nh, nn, nm)) # 큐에 추가
                    visited[nh][nn][nm] = visited[sh][sn][sm] + 1 # 방문 턴 기록
                    ans = visited[nh][nn][nm] # 해당 턴 저장

for h in range(H):
    for n in range(N):
        for m in range(M):
            if data[h][n][m] == 0: # 안 익은 사과
                ans = 0

print(f'{ans - 1}')
