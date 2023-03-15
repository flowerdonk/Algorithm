import sys
from collections import deque
sys.stdin = open('input.txt')

'''
적은 에너지 방법 : 이전 깊이(층)을 모두 채운 경우에만 다음 층으로 넘어감
각 노드가 어느 층에 있는지 확인

[1] 트리 정보 리스트화 -> idx : 자식 노드, val : 부모 노드
[2] 부모노드
'''
# N : 노드 개수, K : 최대 자식 개수, Q : 노드 쌍 개수
N, K, Q = map(int, sys.stdin.readline().rstrip().split()) # 데이터 입력

q = deque()
root = 1 # 시작점부터 끝까지 값을 더해주며 대입할 변수
q.append(root)

# [1] 트리 정보 리스트화 -> idx : 자식 노드, val : 부모 노드
parents = [-1] + [0] * N
while q:
    if root > N: # 노드 수를 넘어가면 반복문 탈출
        break
    parent = q.popleft()

    for k in range(1, K + 1):
        if root + k <= N: # 최대 자식 개수를 더하면서 노드 총합을 벗어나는지 확인
            parents[root + k] = parent # 자식 노드 인덱스에 부모 노드 값 대입
            q.append(root + k) # 큐 추가
    root += K # 노드 다음 층으로 이동

for q in range(Q):
    data = list(map(int, sys.stdin.readline().rstrip().split())) # 데이터 입력
    visited = [-1] + [0] * N # 방문 표시, 1을 넘어가면 중복으로 카운트하지 X
    for n in range(2): # 노드 2개의 거리 모두 계산
        num = data[n]
        while parents[num] != 0: # 루트노드에 도달할 때 까지
            visited[num] += 1 # 방문 표시
            num = parents[num] # 값 변경
    print(visited.count(1)) # 중복되지 않은 값 출력