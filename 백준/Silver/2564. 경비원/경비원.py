L, H = map(int, input().split())
N = int(input())
# 1 : 북쪽(위), 2 : 남쪽(아래), 3 : 서쪽(왼), 4 : 동쪽(오)
# 북, 남 -> 왼쪽부터의 거리 / 동, 서 -> 위쪽부터의 거리
data = [list(map(int, input().split())) for _ in range(N)] # 방향, 거리
x, y = map(int, input().split())

face = {1 : 2, 2 : 1, 3 : 4, 4 : 3}
side = {1 : 3, 2 : 4, 3 : 2, 4 : 1} # 오른쪽 옆

distance = 0
for d in data:
    if d[0] == face[x]: # 마주보고 있을 때
        if x == 1 or x == 2: # 기준점이 위, 아래일 때
            n1 = H + y + d[1]
            n2 = H + 2 * L - y - d[1]
        else: # 기준점이 양 옆일 때
            n1 = L + y + d[1]
            n2 = L + 2 * H - y - d[1]
        n = n1 if n1 <= n2 else n2

    elif d[0] == x: # 같은 변에 있을 때
        n = d[1] - y if d[1] >= y else y - d[1]

    else: # 옆에 있을 때
        if side[x] == d[0]: # 기준점이 더 왼쪽에 있을 때
            if x == 1:  # 기준점이 위일 때
                n = y + d[1]
            elif x == 2: # 아래
                n = L - y + H - d[1]
            elif x == 3: # 왼쪽
                n = H - y + d[1]
            else:
                n = y + L - d[1]

        else:
            if x == 1:  # 기준점이 위일 때
                n = L - y + d[1]
            elif x == 2: # 아래
                n = y + H - d[1]
            elif x == 3: # 왼쪽
                n = y + d[1]
            else:
                n = H - y + L - d[1]

    distance += n
print(distance)