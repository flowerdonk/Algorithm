board_p = [list(map(int, input().split())) for _ in range(5)]
call_p = [list(map(int, input().split())) for _ in range(5)]

board = []
call = []
for p in range(5):
    board += board_p[p]
    call += call_p[p]

bingo_i = [0, 0, 0, 0, 0] # 가로 빙고
bingo_j = [0, 0, 0, 0, 0] # 세로 빙고
cross = [0, 0] # 대각선 우하, 좌하
cnt = 0

for n in range(25):
    if bingo_i.count(5) + bingo_j.count(5) + cross.count(5) >= 3:
        cnt = n
        break

    b_i, b_j = divmod(board.index(call[n]), 5)
    bingo_i[b_i] += 1
    bingo_j[b_j] += 1
    if b_i == b_j:
        cross[0] += 1
    if (b_i, b_j) in [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]:
        cross[1] += 1

print(cnt)