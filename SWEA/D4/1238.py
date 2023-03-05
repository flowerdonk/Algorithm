import sys
sys.stdin = open('input.txt')

'''
T = 10
num = 100
for n in range(1, T + 1):
    N, V = map(int, input().split()) # 입력받는 데이터 길이, 시작점
    arr = list(map(int, input().split())) # (from, to, from, to, ...)
    adjl = {}
    for i in range(N // 2):
        adjl[arr[i * 2]] = adjl.get(arr[i * 2], []) + [arr[i * 2 + 1]]

    print(adjl)
    turn = [1] * num
    visited = [0] * num
    Q = [V]

    while Q:
        pass
'''

def bfs(s):
    # [0] q, visited 및 필요 변수 생성
    q = []
    v = [0] * 101
    ans = s

    # [1] q에 초기데이터 삽입, v 표시
    q.append(s)
    v[s] = 1

    while q:
        # [2] q에서 데이터 한 개 꺼냄 (필요시 정답처리)
        c = q.pop(0)

        if v[ans] < v[c] or v[ans] == v[c] and ans < c:
            ans = c

        # [3] 4/8 연결방향 등 반복처리
        for n in adj[c]:
            if v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1

    return ans

T = 10
for tc in range(1, T + 1):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    # [1] 인접리스트에 연결 저장
    adj = [[] for _ in range(101)]
    for i in range(0, len(lst), 2):
        s, e = lst[i], lst[i + 1]
        adj[s].append(e)

    ans = bfs(S)
    print(f'#{tc} {ans}')