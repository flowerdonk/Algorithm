import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    tree = [0 for _ in range(N + 1)]
    last = 1
    parent = child = 0

    for i in range(len(data)):
        if not tree[i]:  # 아무것도 기록되지 않았으면
            tree[last] = data[i]  # 데이터를 넣어줌
        else:
            last += 1
            child = last  # 새로 추가된 정점을 자식으로
            parent = child // 2  # 완전 이진 트리에서 부모 정점 번호를 구해줌

            tree[child] = data[i]

        # 부모가 있고, 부모가 자식보다 큰 동안 (부모가 작아질 때까지)
        while parent >= 1 and tree[parent] > tree[child]:
            # 부모와 자식 위치를 변경
            tree[parent], tree[child] = tree[child], tree[parent]
            # 자식 위치를 부모로 변경
            child = parent
            parent = child // 2

    sum = 0
    while N >= 1:
        N //= 2
        sum += tree[N]

    print(f'#{tc} {sum}')
