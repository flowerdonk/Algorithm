import sys
N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = [0, 0] # 0 : white, 1 : blue

def cut(x, y, N):
    color = data[x][y] # 왼쪽 위 색상 -> 다른 부분의 색상과 동일한지 확인

    for i in range(x, x + N): # 하나씩 확인
        for j in range(y, y + N):
            if data[i][j] != color: # 다른 색상이 나올 때 4등분으로 나눠서 다시 탐색
                cut(x, y, N // 2) # 왼쪽 위
                cut(x, y + N // 2, N // 2) # 오른쪽 위
                cut(x + N // 2, y, N // 2) # 왼쪽 아래
                cut(x + N // 2, y + N // 2, N // 2) # 오른쪽 아래
                return # 되돌아올 때 벗어나게

    # 반복문을 통과했을 경우 -> 모든 색상이 동일할 경우
    ans[color] += 1 # 해당 색상에 1 추가
    return

cut(0, 0, N)
for n in ans:
    print(n)