import sys
sys.stdin = open('input.txt')

T = int(input())
for i in range(T):
    str1 = input()
    str2 = input()

    if not str1 in str2:
        print(f'#{i + 1} 0')
    else:
        print(f'#{i + 1} 1')