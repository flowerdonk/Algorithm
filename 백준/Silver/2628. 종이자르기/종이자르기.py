L, H = map(int, input().split())
lineN = int(input())
data = [list(map(int, input().split())) for _ in range(lineN)] + [[0, 0], [1, 0], [0, H], [1, L]] # 가로 0, 세로 1 / 점선 번호
data.sort(key = lambda x : x[1])
data_l = []
data_h = []
for n in range(len(data)):
    if data[n][0] == 0:
        if not data_l:
            data_l.append(data[n][1])
        else:
            data_l.append(data[n][1] - past_l)
        past_l = data[n][1]
    else:
        if not data_h:
            data_h.append(data[n][1])
        else:
            data_h.append(data[n][1] - past_h)
        past_h = data[n][1]

ans = max(data_l) * max(data_h)
print(ans)