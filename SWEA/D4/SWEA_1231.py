import sys
sys.stdin = open('input.txt')

# 중위순회
def inorder(i):
    if i > 0:
        inorder(c1[i])
        print(l[i], end='')
        inorder(c2[i])

T = 10

for tc in range(1, T + 1):
    N = int(input())
    data = [list(input().split()) for _ in range(N)]
    data.insert(0, [0, 0, 0, 0])  # 노드는 1번부터, 0번째에 빈 리스트 추가
    for i in data:
        # 자식이 없거나 하나인 경우, 크기를 맞추기 위해 0 추가
        while len(i) != 4:
            i.append('0')

    c1 = [0] * (N + 1)
    c2 = [0] * (N + 1)
    l = [''] * (N + 1) # 알파벳을 받을 

    for n in data:
        # v - 부모 노드, letter - 글자, lv - 왼쪽 자식, rv - 오른쪽 자식
        v, letter, lv, rv = int(n[0]), n[1], int(n[2]), int(n[3])

        c1[v] = lv
        c2[v] = rv
        l[v] = letter

    print(f'#{tc}', end =' ')
    inorder(1)
    print()


