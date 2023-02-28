import sys
sys.stdin = open('input.txt')

L, H = map(int, input().split())
N = int(input())
# 1 : 북쪽(위), 2 : 남쪽(아래), 3 : 서쪽(왼), 4 : 동쪽(오)
# 북, 남 -> 왼쪽부터의 거리 / 동, 서 -> 위쪽부터의 거리
data = [list(map(int, input().split())) for _ in range(N)] # 방향, 거리
x, y = map(int, input().split())

face = {1 : 2, 2 : 1, 3 : 4, 4 : 1}

distance = 0
for d in data:
    if d[0] == face[x]: # 마주보고 있을 때
        n1 = H + x + d[1]
        n2 = H + 2 * L - x - d[1]
        n = n1 if n1 <= n2 else n2
        distance += n
    elif d[0] == x:
        n = d[1] - y if
        distance +=
    else:
        pass