T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    decode = {'1011000' : 0, '1001100' : 1, '1100100' : 2, '1011110' : 3, '1100010' : 4, '1000110' : 5, '1111010' : 6, '1101110' : 7, '1110110' : 8, '1101000' : 9}

    for d in data:
        if '1' in d:
            code = ''.join(reversed(d)) # 암호가 있는 행 찾기, 이를 역순으로
            break

    start_idx = code.index('1') # 첫 '1' 인덱스

    result = [] # 결과 숫자 담을 리스트
    idx = start_idx
    while len(result) != 8: # 8개 숫자가 담기면 종료
        mid = ''
        for i in range(7):
            mid += code[idx + i] # 7개 문자 담기
        result.append(decode[mid]) # decode에서 값 찾기
        idx += 7 # 그 다음 숫자로 이동

    result.reverse() # 다시 원래 방향으로

    odd = 0
    eve = 0
    for n in range(4):
        odd += int(result[n * 2])
        eve += int(result[n * 2 + 1])

    ans = odd * 3 + eve
    print(f'#{tc}', end = ' ')
    if not ans % 10:
        print(odd + eve)
    else:
        print(0)