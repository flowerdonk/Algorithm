import sys
sys.stdin = open('input.txt')

def Winner(arr):
    P = arr[0]
    A = arr[1]
    B = arr[2]

    startA = startB = 1
    endA = endB = P

    while startA <= endA and startB <= endB:
        middleA = (startA + endA) // 2
        middleB = (startB + endB) // 2

        if middleA == A and middleB == B:
            return '0'
        elif middleA == A:
            return 'A'
        elif middleB == B:
            return 'B'

        if middleA > A:
            endA = middleA # 왼쪽으로 이동
        if middleB > B:
            endB = middleB # 왼쪽으로 이동

        if middleA < A:
            startA = middleA # 왼쪽으로 이동
        if middleB < B:
            startB = middleB # 왼쪽으로 이동

    return False # 검색 실패


T = int(input())
result = []
for i in range(T):
    arr = list(map(int, input().split()))
    result.append(Winner(arr))

for i in range(T):
    print(f'#{i + 1} {result[i]}')


