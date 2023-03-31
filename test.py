import heapq
INF = int(1e9) # 무한 값

v, e = map(int, input().split()) # 노드 개수, 간선 개수
first = int(input()) # 시작 노드 번호
graph = [[] for _ in range(v + 1)] # 연결 노드 관계 리스트
distance = [INF] * (v + 1) # 최단 거리, 무한으로 초기화

for _ in range(e):
    start, end, cost = map(int, input().split()) # start에서 end까지의 비용 cost
    graph[start].append((end, cost))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 시작 노드로 가기 위한 최단 경로 0 설정, 큐에 삽입
    distance[start] = 0 # 시작 노드 초기화

    while q: # 큐가 비어있지 않으면
        dist, now = heapq.heappop(q) # 최단 거리가 가장 짧은 노드 꺼내기

        if distance[now] < dist: # 현재 노드가 이미 처리된 적이 있는 노드면 무시
            continue

        for i in graph[now]: # 현재 노드 인접 노드 확인
            cost = dist + i[1]

            if cost < distance[i[0]]: # 현재 노드를 거쳐 이동하는 거리가 더 짧은 경우
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(first)

for i in range(1, v + 1): # 1노드부터의 최단 거리 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

