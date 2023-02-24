N = int(input()) # 주사위의 개수
dices = [list(map(int, input().split())) for _ in range(N)] # 주사위 종류
updown = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0} # 마주보는 주사위 인덱스
mx = 0 # 최댓값
# 현재 주사위 아래 인덱스 -> 현재 주사위 위 인덱스 -> 현재 주사위 위 값 -> 다음 주사위 아래 값 -> 다음 주사위 아래 인덱스 반복
for fst_idx in range(6): # 맨 아래 주사위 변경
    total = 0 # 총합
    down_idx = fst_idx # 아래 인덱스
    up_idx = updown[fst_idx] # 위 인덱스
    for build in range(N): # 옆면을 바꿔야할 주사위 총 개수 = 전체 개수
        down = dices[build][down_idx] # 현재 주사위 아래 값
        up = dices[build][up_idx] # 현재 주사위 위 값
        sides = list(set(dices[build]) - set([down, up])) # 주사위에서 위 아래 값 제거
        face = max(sides) # 옆면 중 최대값
        total += face # 총합 구하기 위함
        if build <= N - 2: # 마지막 주사위 직전까지 위 아래 값 찾기
            down_idx = dices[build + 1].index(up) # 아래 인덱스 -> 전 주사위 위 값을 가진 다음 주사위 아래 인덱스
            up_idx = updown[down_idx] # 위 인덱스

    if mx <= total: # 최댓값 갱신
        mx = total

print(mx)
