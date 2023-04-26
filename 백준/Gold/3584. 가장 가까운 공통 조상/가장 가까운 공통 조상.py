T = int(input())
for tc in range(T):
    N = int(input())
    parent = [-1] + [0] * (N)

    '''
    [1] A가 B의 부모
    parent : idx 자식노드, val 부모노드
    '''
    for n in range(N - 1):
        A, B = map(int, input().split())
        parent[B] = A
    start, end = map(int, input().split())

    # 자기 자신 넣기(자기 자신이 최소 조상 노드일 경우)
    s_ancestor = [start]
    e_ancestor = [end]
    
    '''
    [2] 부모노드를 따라 올라가며 조상노드 정보 모두 저장
    '''
    while parent[start]:
        s_ancestor.append(parent[start])
        start = parent[start] # 시작점 갱신

    while parent[end]:
        e_ancestor.append(parent[end])
        end = parent[end] # 시작점 갱신
        
    '''
    [3] 거리 최소, 공통 조상 구하기
    '''
    dist = 100000
    ans = 0

    for s in range(len(s_ancestor)):
        for e in range(len(e_ancestor)):
            if s_ancestor[s] == e_ancestor[e]:
                if dist > (s + e + 2): # 최소값 갱신
                    ans = s_ancestor[s]
                    dist = s + e + 2

    print(ans)