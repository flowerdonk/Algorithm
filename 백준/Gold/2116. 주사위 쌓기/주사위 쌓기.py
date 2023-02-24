# 주사위 갯수 입력
Dice_num = int(input())

# 주사위 종류 입력, 2차원 리스트
Dices = [] * Dice_num
for i in range(Dice_num):
    Dices.append(list(map(int, input().split())))

# 주사위 종류를 입력받은 후, 함수 정의
# 주사위 1개, 아랫값을 입력받아 최대 옆면 값, 반대 값 리턴하는 함수
def find_maxside_bottom(Dice, bottom):
    for i in range(6): # 인덱스 순환
        if Dice[i] == bottom: # 아랫값을 가진 인덱스 찾기
            idx = i # 인덱스
            break
    
    # (최대 옆면 값, 반대 값) 리턴
    if idx == 1:
        return (max(Dice[0], Dice[2], Dice[4], Dice[5]), Dice[3])
    elif idx == 2:
        return (max(Dice[0], Dice[1], Dice[3], Dice[5]), Dice[4])
    elif idx == 3:
        return (max(Dice[0], Dice[2], Dice[4], Dice[5]), Dice[1])
    elif idx == 4:
        return (max(Dice[0], Dice[1], Dice[3], Dice[5]), Dice[2])
    elif idx == 5:
        return (max(Dice[1], Dice[2], Dice[3], Dice[4]), Dice[0])
    elif idx == 0:
        return (max(Dice[1], Dice[2], Dice[3], Dice[4]), Dice[5])


max_sum = 0 # 최종 최대값
for i in range(1, 7): # 1 ~ 6 주사위 값
    bottom = i # 맨 아랫값 설정
    total = 0

    for num in range(Dice_num):
        max_side, bottom = find_maxside_bottom(Dices[num], bottom) # 최대 옆면 값, 반대 값 = t번째 주사위, 아랫값
        total += max_side # 옆면 값 총합

    if max_sum <= total: # 최종 최대값 갱신
        max_sum = total

print(max_sum)