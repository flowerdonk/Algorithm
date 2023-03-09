from collections import deque
import sys
sys.stdin = open('input.txt')

<<<<<<< HEAD
N = int(input())
data = [list(map(int, input().split())) for _ in range(N - 1)]
=======
'''
이진트리가 아닌 트리 구조
리프부터 루트까지 거리 확인
'''

N = int(input())
data = [list(map(int, input().split())) for _ in range(N - 1)]
parents = [-1] + [0 for _ in range(N)] # idx : 자식노드, val : 부모노드
temp = [[] for _ in range(N + 1)] # idx : 부모노드, val : 자식노드
q = deque() # 자식노드 저장할 queue
leaf = [] # leaf노드 저장할 queue
visited = [0] * (N - 1) # 방문표시 -> 정렬 불가, idxerror 방지
ans = 0

# root의 자식노드 찾기
for n in range(N - 1):
    if 1 in data[n]: # root가 있을 때
        child = data[n][0] if data[n][1] == 1 else data[n][1] # 1이 아닌 다른 요소가 자식노드
        q.append(child) # 시작점 추가
        visited[n] += 1 # 방문 표시
        parents[child] = 1 # 부모 표시
        temp[1].append(child)

# parents 형성
while q:
    parent = q.popleft() # 자식노드 -> 부모노드

    for n in range(N - 1):
        if parent in data[n] and visited[n] == 0: # 부모노드의 자식노드 찾기
            child = data[n][0] if data[n][1] == parent else data[n][1] # 부모노드가 아닌 다른 요소가 자식노드
            parents[child] = parent # 부모 표시
            q.append(child) # 자식 노드 추가
            visited[n] += 1 # 방문 표시
            temp[parent].append(child)

for n in range(1, N + 1): # leaf 찾기
    if len(temp[n]) == 0:
        leaf.append(n)


print(ans)
>>>>>>> 82b860b0731ed7305066433f8c315caa43adb8d8
