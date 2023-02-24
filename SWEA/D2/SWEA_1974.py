import sys
sys.stdin = open('input.txt')

def Puzzle(arr):
    for lst in arr:
        if len(set(lst)) != 9:
            return 0

    arr_t = list(zip(*arr))
    for lst in arr_t:
        if len(set(lst)) != 9:
            return 0

    for i in (0, 3, 6):
        for j in (0, 3, 6):
            lst = arr[i][j:j + 3] + arr[i + 1][j:j + 3] + arr[i + 2][j:j + 3]
            if len(set(lst)) != 9:
                return 0

    return 1

T = int(input())
for i in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    ans = Puzzle(arr)
    print(f'#{i} {ans}')