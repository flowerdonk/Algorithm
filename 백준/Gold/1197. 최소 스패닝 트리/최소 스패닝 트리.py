def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)

V, E = map(int, input().split()) # 0 ~ V: 정점번호, E: 간선 수
rep = [i for i in range(V + 1)]
graph = []

for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph.append([v1, v2, w])

# [1] 가중치 기준 오름차순 정렬
graph.sort(key=lambda x:x[2])

# [2] N개의 정점(V + 1)에 대해서, N - 1개의 간선 선택
N = V + 1
s = 0 # MST에 포함된 간선의 가중치 합
cnt = 0 # 선택
MST = []
for u, v, w in graph: # 가중치가 작은 것부터
    # 두 개의 대표 원소를 찾고 비교
    if find_set(u) != find_set(v): # 사이클이 생기지 않으면
        cnt += 1
        s += w # 가중치 합
        MST.append([u, v, w])
        union(u, v)
        if cnt == N - 1: # MST 구성 완료
            break

print(s) # 175