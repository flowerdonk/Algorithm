def Card(Card_N, Number):
    max_card = 0 # 최대 카드 값
    max_num = 0 # 장 수
    count_list = [0] * 10 # 카운팅 정렬

    for letter in Number: # 숫자 하나씩 확인
        count_list[letter] += 1 # 인덱스를 따라 +1
    
    for idx in range(len(count_list)): # 카운팅 정렬 확인
        if count_list[idx] >= max_num: # 최댓값 찾기, =추가함으로 동일 수이면 뒷 번호로 갱신
            max_card = idx # 인덱스가 최대 카드 값
            max_num = count_list[idx] # 장 수

    return (max_card, max_num)

T = int(input()) # 테스트 케이스 수
Card_Ns = [] # 카드 장수 리스트
Numbers = [] # 카드 번호 리스트-리스트

for i in range(T):
    Card_Ns.append(int(input()))
    Numbers.append(list(map(int, list(input()))))

for i in range(T):
    max_card, max_num = Card(Card_Ns[i], Numbers[i]) # 인풋 그룹 하나씩 전달
    print(f'#{i + 1} {max_card} {max_num}')