import sys
sys.stdin = open('input.txt')

def postorder(n):
    if n > 0:
        n1 = postorder(node[n * 2])
        n2 = postorder(node[n * 2 + 1])
        return (n1 + n2)


T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split()) # N : 노드 개수, M : 리프 노드 개수, L : 출력 노드 번호
    data = [list(map(int, input().split())) for _ in range(M)]

    node = [0] * (N + 1)
    for n in range(M):
        node[data[n][0]] = data[n][1]
    print(node)

    print(postorder(1))
