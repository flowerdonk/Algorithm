import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    parent = [[] for _ in range(N + 1)]
    ancestor = [[] for _ in range(N + 1)]
    # A가 B의 부모
    for n in range(N - 1):
        A, B = map(int, input().split())
        parent[B].append(A)
    start, end = map(int, input().split())
    for node in range(N + 1):
        stack = [parent[node]]
        ancestor[node].append(parent[node])
        while stack:
            next_node = stack.pop()
            ancestor[parent[node]].append(next_node)
            stack.append(next_node)
    print(ancestor) # 끝은 무조건 8(루트)