def switch(idx): # 스위치 상태 변경
    if switches[idx] == 1:
        switches[idx] = 0
    else:
        switches[idx] = 1

switchN = int(input()) # 스위치 개수
switches = list(map(int, input().split())) # 스위치 상태
studentN = int(input()) # 학생수
students = [list(map(int, input().split())) for _ in range(studentN)] # [성별(남 1, 여 2), 받은 수]

for n in range(studentN):
    s = students[n][0] # 성별
    idx = students[n][1] - 1 # 받은 수
    if s == 1: # 남학생 : 자기가 받은 수의 배수 번호의 상태 변경
        for i in range(idx, switchN, idx + 1): # 받은 수 부터 끝까지 배수만큼씩 이동
            switch(i)
    else: # 여학생 : 자기가 받은 수를 중심으로 좌우 대칭, 가장 많은 스위치를 포함하는 구간의 스위치 상태 변경
        switch(idx)
        li = idx - 1 # 왼쪽으로
        ri = idx + 1 # 오른쪽으로 인덱스 이동
        while 0 <= li < idx and idx < ri < switchN: # 양 옆 인덱스가 범위 내
            if switches[li] == switches[ri]: # 스위치가 같으면
                switch(li) # 변경
                switch(ri)
                li -= 1 # 왼쪽으로 이동
                ri += 1 # 오른쪽으로 이동
            else:
                break

for l in range(switchN):
    if l != 0 and l % 20 == 0:
        print()
    print(switches[l], end = ' ')