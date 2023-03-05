import sys
sys.stdin = open('input.txt')

def node(adjL, S, G):
    visited = [0] * (V + 1)
    Q = [S]
    visited[S] = 1

    while Q:
        t = Q.pop(0)

        for v in adjL[t]:
            if visited[v] == 0:
                Q.append(v)
                visited[v] = visited[t] + 1
                if v == G:
                    return visited[G] - 1

    return 0 # 방문 안했을 때

T = int(input())
for i in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    adjL = [[] for _ in range(V + 1)] # 인접 리스트
    for a in arr:
        adjL[a[0]].append(a[1])
        adjL[a[1]].append(a[0])

    print(f'#{i} {node(adjL, S, G)}')