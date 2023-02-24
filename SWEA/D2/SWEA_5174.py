import sys
sys.stdin = open('input.txt')

def postorder(i):
    global cnt # 방문횟수
    if i > 0:
        postorder(left[i])
        cnt += 1
        postorder(right[i])

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    left = [0] * (E + 2) # 왼쪽 자식
    right = [0] * (E + 2) # 오른쪽 자식
    for n in range(len(arr) // 2):
        p, c = arr[n * 2], arr[n * 2 + 1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    cnt = 0
    postorder(N) # 시작점을 루트로
    print(f'#{tc} {cnt}')


