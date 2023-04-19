import heapq
INF = 1000001

N, M, K, X = map(int, input().split())
node = [[] for _ in range(N + 1)]
dist = [INF] * (N + 1)
for _ in range(M):
    s, e = map(int, input().split())
    node[s].append(e)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        d, now = heapq.heappop(q)

        if dist[now] < d:
            continue

        for i in node[now]:
            cost = d + 1

            if cost < dist[i]:
                dist[i] = cost
                heapq.heappush(q, (cost, i))

dijkstra(X)
flag = 0
for n in range(1, N + 1):
    if dist[n] == K:
        flag = 1
        print(n)

if flag == 0:
    print(-1)