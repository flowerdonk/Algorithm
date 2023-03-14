import sys
from collections import deque
sys.stdin = open('input.txt')

'''
적은 에너지 방법 : 이전 깊이(층)을 모두 채운 경우에만 다음 층으로 넘어감
각 노드가 어느 층에 있는지 확인

[1] 트리 정보 리스트화
[2] 부모노드
'''
# N : 노드 개수, K : 최대 자식 개수, Q : 노드 쌍 개수
N, K, Q = map(int, sys.stdin.readline().rstrip().split()) # 데이터 입력
data = []
for q in range(Q):
    data.append(list(map(int, sys.stdin.readline().rstrip().split())))

q = deque()
root = 1
q.append(root)

parents = [-1] + [0] * N
while q:
    if root > N:
        break
    parent = q.popleft()

    for k in range(1, K + 1):
        if root + k <= N:
            parents[root + k] = parent
            q.append(root + k)
    root += K

for d in data:
    visited = [-1] + [0] * N
    for n in range(2):
        num = d[n]
        while parents[num] != 0:
            visited[num] += 1
            num = parents[num]
    print(visited.count(1))