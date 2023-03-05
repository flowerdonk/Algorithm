import sys
sys.stdin = open('input.txt')

def GNS(N, arr):
    NUM = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    result = [[] for _ in range(10)]

    for i in range(N):
        letter = NUM.index(arr[i])
        result[letter].append(arr[i])

    return result

T = int(input())

for i in range(T):
    Tcase = list(input().split())
    TcaseN = int(Tcase[1])
    arr = list(input().split())
    Ans = GNS(TcaseN, arr)

    print(Tcase[0])
    for num in Ans:
        print(*num, end = ' ')
    print()