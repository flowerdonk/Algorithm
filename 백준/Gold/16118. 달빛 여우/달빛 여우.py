import sys
input = sys.stdin.readline

from heapq import heappush, heappop
INF = int(1e9)

def fox_dijkstra():
    q = []
    heappush(q, (0, 1)) # 거리, 도착점
    distance_fox[1] = 0 # 시작 노드 초기화

    while q: # 큐가 비어있지 않으면
        dist, now = heappop(q) # 최단 거리가 가장 짧은 노드 꺼내기

        if distance_fox[now] < dist: # 이미 처리된 노드면 무시
            continue

        for ni, di in graph[now]:
            cost = dist + di
            if cost < distance_fox[ni]:
                distance_fox[ni] = cost
                heappush(q, (cost, ni))

def wolf_dijkstra():
    q = []
    heappush(q, (0, 1, False)) # 거리, 도착점, 턴
    distance_wolf[1][1] = 0 # 시작 노드 초기화, distance_wolf[0] 빠르게 도착, distance_wolf[1] 느리게 도착

    while q: # 큐가 비어있지 않으면
        dist, now, turn = heappop(q) # 최단 거리가 가장 짧은 노드 꺼내기

        if turn and distance_wolf[0][now] < dist: # 이미 처리된 노드면 무시
            continue
        elif not turn and distance_wolf[1][now] < dist:
            continue

        for ni, di in graph[now]:
            if turn: # 홀수번째면
                cost = dist + di * 2
                if cost < distance_wolf[1][ni]:
                    distance_wolf[1][ni] = cost
                    heappush(q, (cost, ni, False))
            else:
                cost = dist + di // 2
                if cost < distance_wolf[0][ni]:
                    distance_wolf[0][ni] = cost
                    heappush(q, (cost, ni, True))

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance_fox = [INF] * (N + 1)
distance_wolf = [[INF] * (N + 1) for _ in range(2)]

for _ in range(M):
    a, b, d = map(int, input().split())
    graph[a].append((b, d * 2)) # a -> b 거리 d
    graph[b].append((a, d * 2)) # b -> a 거리 d

fox_dijkstra()
wolf_dijkstra()

answer = 0
for i in range(1, N+1):
    if distance_fox[i] < min(distance_wolf[0][i], distance_wolf[1][i]):
        answer += 1
print(answer)