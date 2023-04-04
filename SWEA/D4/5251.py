import sys
sys.stdin = open('input.txt')

def dijkstra(s, V):
    U = [0] * (V + 1)
    U[s] = 1

    for i in range(V + 1):
        D[i] = adjM[s][i]

    N = V + 1
    for _ in range(N - 1):
        minV = INF
        w = 0
        for i in range(N):
            if U[i] == 0 and minV > D[i]:
                w = i
                minV = D[i]
        U[w] = 1

        for v in range(N):
            if 0 < adjM[w][v] < INF:
                D[v] = min(D[v], D[w] + adjM[w][v])

INF = 10001
T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adjM = [[INF] * (V + 1) for _ in range(V + 1)]
    for i in range(V + 1):
        adjM[i][i] = 0
    for _ in range(E):
        u, v, w = map(int, input().split())
        adjM[u][v] = w

    D = [0] * (V + 1)
    dijkstra(0, V)
    print(f'#{tc} {D[-1]}')