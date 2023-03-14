import sys
from collections import deque

N = int(input())
nodes = [[] for _ in range(N + 1)]
parents = [0] * (N + 1)
visited = [0] * (N + 1)
for n in range(N - 1):
    n1, n2 = map(int, sys.stdin.readline().rstrip().split())
    nodes[n1].append(n2)
    nodes[n2].append(n1)

q = deque()
for r in nodes[1]:
    q.append(r)
    parents[r] = 1
visited[1] = 1

while q:
    parent = q.popleft()
    visited[parent] = 1
    for c in nodes[parent]:
        if visited[c] != 1:
            parents[c] = parent
            q.append(c)

for n in range(2, N + 1):
    print(parents[n])