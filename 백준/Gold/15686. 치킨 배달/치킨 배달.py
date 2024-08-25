N, M = map(int, input().split())
house = []
chicken = []
min_dist = 99999

for i in range(N):
    temp = tuple(input().split())
    for j in range(N):
        if temp[j] == '1':
            house.append((i, j))
        elif temp[j] == '2':
            chicken.append((i, j))

visited = [False] * len(chicken)

def dfs(idx, cnt):
    global min_dist
    # M개 선택 완료
    if cnt == M:
        total_dist = 0
        for h in house:
            temp_dist = 99999
            # 거리 계산
            for n in range(len(chicken)):
                if visited[n]:
                    dist = abs(chicken[n][0] - h[0]) + abs(chicken[n][1] - h[1])
                    # 최소 거리
                    temp_dist = min(dist, temp_dist)
            # 치킨 거리
            total_dist += temp_dist
        # 최솟값 갱신
        min_dist = min(total_dist, min_dist)
        return
    # dfs
    for i in range(idx, len(chicken)):
        visited[i] = True
        dfs(i + 1, cnt + 1)
        visited[i] = False

dfs(0, 0)

print(min_dist)