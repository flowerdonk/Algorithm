# 0(출발점) -> N(종점)
# 한 번에 이동할 수 있는 최대 정류장 수 k
# 충전기가 설치된 정류장 M개, 번호 인풋 (출발지에는 충전기 설치 O, 충전횟수 포함 X)
# 잘못 설치되어 종점에 도착할 수 없는 경우 0 출력
# 종점에 도착하기 위해 필요한 최소한의 충전 횟수 출력

def Bus(KNM, M_list): # 최대 정류장 수, 종점, 충전기 # 충전기 정류장 번호 리스트
    charge = 0 # 충전 횟수
    position = 0 # 버스의 위치
    K = KNM[0] # 이동 가능한 최대 정류장 수
    N = KNM[1] # 종점 위치
    M = KNM[2] # 충전기 정류장 수
    
    while position < N: # 위치가 종점보다 작을 때
        if position + K >= N: # 반복하다가 위치 + 이동 가능 수가 종점을 넘으면
            return charge # 충전 횟수 그대로 리턴

        if position + K in M_list: # 위치 + 이동 가능 수가 충전기 정류장일 때
            position += K # 이동 가능 최대수 만큼 이동
            charge += 1 # 충전 횟수 +1
            continue # 해당 반복 턴 종료
        else:
            check = 0 # 이동 여부
            for i in range(K - 1, 0, -1): # 위치에 1부터 k - 1까지 더함
                if position + i in M_list:
                    position += i
                    charge += 1
                    check += 1
                    break
            if check == 0: # 이동을 안했을 경우
                return 0 # 0 리턴

    return charge


T = int(input()) # 노선 수(테스트 케이스 수)
KNMs = [] # 한 번 이동 최대 정류장 수, 종점, 충전기 설치 정류장 리스트
M_lists = [] # 충전기 정류장 번호 리스트

for i in range(T):
    KNMs.append(list(map(int, input().split())))
    M_lists.append(list(map(int, input().split())))

for i in range(T):
    charges = Bus(KNMs[i], M_lists[i]) # 인풋 그룹 하나씩 전달
    print(f'#{i + 1} {charges}')