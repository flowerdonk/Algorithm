N, K = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)] # 0:여, 1:남 / 학년
room = [[0, 0] for _ in range(6)]

for d in data:
    if d[0] == 0:
        room[d[1] - 1][0] += 1
    else:
        room[d[1] - 1][1] += 1

cnt = 0
for r in room:
    for n in r:
        if n % K == 0:
            cnt += n // K
        else:
            cnt += n // K + 1

print(cnt)