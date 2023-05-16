'''
[0] 이동 규칙
시작점 -> 왼쪽 가장 위
도착점 -> 오른쪽 가장 아래
최단 거리로 가기 때문에 이동하는 방향은 무조건 오른쪽 혹은 아래
'''
N, M = map(int, input().split()) # 행, 열
K = int(input()) # 공사 중인 도로 개수

'''
[1] DP
양 끝 점이 N, M 이므로 인덱스를 생각하여 각각 +1 까지
[[경우의 수, [아래 이동 가능 여부, 오른쪽 이동 가능 여부]] * (M + 1) ] * (N + 1)
'''
DP = [[[0, [True, True]] for _ in range(M + 1)] for _ in range(N + 1)]
DP[0][0][0] = 1 # 시작점(0, 0)의 경우의 수는 1

for _ in range(K):
    '''
    [2] 막힌 도로
    좌표가 주어질 때, 그 도로의 방향이 오른쪽인지 아래인지 정해지지 않음
    DP에 저장하기 위해서는 이를 판별해줘야 함
    '''
    a, b, c, d = map(int, input().split()) # 막힌 도로의 좌표
    # 공사 중인 도로의 길이는 최대 1
    # (a == c && b != d) || (a != c && b == d) 성립
    if a > c:
        a, c = c, a # 큰 값을 뒤로
    if b > d:
        b, d = d, b
    check = 0 if c - a > d - b else 1 # 0: 아래가 막힌 경우, 1: 오른쪽이 막힌 경우
    DP[a][b][1][check] = False # 도로 막기

direction = [(1, 0), (0, 1)] # 아래 이동, 오른쪽 이동
for n in range(N + 1):
    for m in range(M + 1):
        for d in range(2): # 이동 가능한 방향 2가지
            nn, nm = n + direction[d][0], m + direction[d][1]
            if nn <= N and nm <= M and DP[n][m][1][d]: # 범위 내 + 공사중이 아니라면(True)
                DP[nn][nm][0] += DP[n][m][0] # 경우의 수 더하기

print(DP[N][M][0])