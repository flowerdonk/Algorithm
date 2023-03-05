import sys
sys.stdin = open('input.txt')

def count(arr):
    ans = 0
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1: # 단어를 넣을 수 있는 공백
                cnt += 1
            else: # 칸 없음
                if cnt == K:
                    ans += 1
                cnt = 0
    return ans

T = int(input())
for i in range(1, T + 1):
    N, K = map(int, input().split())
    # 오른쪽 끝, 아래에 0 추가
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 1)]
    # 정치 행렬
    arr_t = list(map(list, zip(*arr)))

    ans = count(arr) + count(arr_t)
    print(f'#{i} {ans}')