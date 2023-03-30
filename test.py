import sys
sys.stdin = open('input.txt')

def qsort(A, start, end):
    if start >= end:
        return
    pivot = start    # 첫 번째 원소
    left = start + 1 # 피봇보다 큰 값을 찾을 때까지 오른쪽 이동, 피봇 다음 값
    right = end      # 피봇보다 작은 값을 찾을 때까지 왼쪽 이동

    # 교차 X
    while left <= right:
        while left <= right and A[left][0] <= A[pivot][0]:  # 큰 값을 마주치면 벗어남
            if A[left][0] == A[pivot][0]:                   # x가 같은 값일 경우
                if A[left][1] > A[pivot][1]:                # y가 더 크면 벗어남 -> 더 큰 수
                    break
            left += 1                                       # 큰 값 찾을 때까지 오른쪽으로 이동
        while left <= right and A[right][0] >= A[pivot][0]: # 작은 값을 마주치면 벗어남
            if A[right][0] == A[pivot][0]:                  # x가 같은 값을 경우
                if A[right][1] < A[pivot][1]:               # y가 더 작으면 벗어남 -> 더 작은 수
                    break
            right -= 1                                      # 작은 값을 찾을 때까지 왼쪽으로 이동

        # 교차 X
        if left < right:
            A[left], A[right] = A[right], A[left]
    # 교차 O
    else:
        A[pivot], A[right] = A[right], A[pivot]              # 이후 반복문 탈출

    qsort(A, start, right - 1)
    qsort(A, right + 1, end)

N = int(sys.stdin.readline())
data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))
qsort(data, 0, N - 1)

for n in range(N):
    print(*data[n])