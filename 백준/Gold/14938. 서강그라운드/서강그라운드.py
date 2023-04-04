INF = 3001 # 무한

n, m, r = map(int, input().split()) # n: 지역 개수, m: 수색 범위, r: 길 개수
items = [0] + list(map(int, input().split())) # 각 구역의 아이템 수
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용 -> 0
for i in range(1, n + 1):
    graph[i][i] = 0

# 각 간선에 대한 정보 입력, 그 값으로 초기화
for _ in range(r):
    # A -> B 비용은 C
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

ans = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            ans[i] += items[j]
print(max(ans))