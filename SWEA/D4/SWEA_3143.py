import sys
sys.stdin = open('input.txt')

def text(A, B):
    cnt = 0

    for i in range(len(A) // len(B)):
        if B in A:
            cnt += 1
            A = A.replace(B, '', 1)

    result = cnt + len(A)
    return result

T = int(input())
for i in range(1, T + 1):
    A, B = input().split()
    print(f'#{i} {text(A, B)}')
