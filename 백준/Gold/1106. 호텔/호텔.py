C, N = map(int, input().split()) # 목표 고객 수, 도시 수
cities = [tuple(map(int, input().split())) for _ in range(N)] # (홍보 비용, 얻는 고객 수)
dp = [1e7] * (C + 100) # idx: 확보 고객 수, val: 최소 비용
dp[0] = 0

for cost, num in cities:
    for i in range(num, C + 100): # 고객 수 단위로 확인, 시작 점은 처음 X(이전 값과 비교해야 함)
        dp[i] = min(dp[i - num] + cost, dp[i])

print(min(dp[C:]))