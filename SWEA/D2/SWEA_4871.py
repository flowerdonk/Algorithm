def nod(S):
    visited[S] = 1

    for w in range(1, V + 1):
        if arr[S][w] == 1 and visited[w] == 0:
            nod(w)

    return visited

T = int(input())
for m in range(1, T + 1):
    V, E = map(int, input().split()) # 노드 수, 간선 수
    nodes = []
    for n in range(E):
        nodes.append(list(map(int, input().split())))
    S, G = map(int, input().split())

    visited = [0] * (V + 1)
    arr = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        n1, n2 = nodes[i]
        arr[n1][n2] = 1

    ans = nod(S)
    if ans[G] == 1:
        print(f'#{m} 1')
    else:
        print(f'#{m} 0')