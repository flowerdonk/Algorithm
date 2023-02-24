import sys
sys.stdin = open('input.txt')

# 1 : 가위, 2 : 바위, 3 : 보
# 같은 카드일 경우 번호가 작은 쪽이 승자

def card(arr, begin, end):
    if begin < end:
        p = partition(arr, begin, end)
        card(arr, begin, p - 1)
        card(arr, p + 1, end)

def partition(arr, begin, end):
    pivot = (begin + end) // 2 # 피봇 키
    L = begin
    R = end

    while L < R:
        while (L < R and arr[L] < arr[pivot]):
            L += 1
        while (L < R and arr[R] < arr[pivot]):
            R -= 1

        if L < R:
            if L == pivot:
                pivot = R
                arr[L], arr[R] = arr[R], arr[L]

    arr[pivot], arr[R] = arr[R], arr[pivot]

    return R

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    arr = list(enumerate(map(int, input().split()))) # [번호 - 1, 카드 값]
    card(arr, 0, N - 1)
    print(f'#{i} {arr[-1]}')