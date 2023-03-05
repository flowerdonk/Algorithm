import sys
sys.stdin = open('input.txt')

# 중위 순회
def inorder(i):
    global cnt
    if i > 0 and i <= N:
        inorder(left[i])
        result[i] = cnt # 중위 순회로 찾은 첫번째 지점부터 끝까지에 cnt 값 추가
        cnt += 1
        inorder(right[i])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = [0] * (N + 1) # 노드 위치에 결과 값을 넣을 리스트
    # 자식 노드 (부모 인덱스)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for n in range(1, N // 2 + 1):
        left[n] = n * 2 # 왼쪽 자식 노드
        if n * 2 + 1 <= N: # 오른쪽 자식 노드가 없을 경우를 대비
            right[n] = n * 2 + 1

    cnt = 1 # 번호는 1부터 시작, 1씩 증가
    inorder(1) # 루트부터 시작

    print(f'#{tc}', result[1], result[N//2])


'''
자식노드 리스트 형성 없이 구현

def inorder(i, N):
    global cnt
    if i <= N:
        inorder(i * 2, N)
        result[i] = cnt
        cnt += 1
        inorder(i * 2 + 1, N)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = [0] * (N + 1)

    cnt = 1
    inorder(1, N)

    print(f'#{tc}', result[1], result[N//2])
'''
