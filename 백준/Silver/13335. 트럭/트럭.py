from collections import deque

N, W, L = map(int, input().split())         # 트럭 수, 다리 길이, 최대 하중
trucks = list(map(int, input().split()))    # 트럭 무게
time = 0                                    # 시간
cnt = 0                                     # 다리 위 무게
idx = 0                                     # 트럭 인덱스

# 다리 길이만큼 0 삽입 (시간 계산)
que = deque()
for _ in range(W):
    que.append(0)

# 큐가 빌 때 까지
while(que):
    cnt -= que.popleft()
    time += 1

    # 트럭이 남은 경우
    if idx < N:
        # 최대 하중 고려
        if cnt + trucks[idx] <= L:
            que.append(trucks[idx])
            cnt += trucks[idx]
            idx += 1
        else:
            que.append(0)

print(time)