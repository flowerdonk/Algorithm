import sys
sys.stdin = open('input.txt')

N = int(input()) # 기둥 개수
buildings = [list(map(int, input().split())) for _ in range(N)] # [기둥 인덱스, 높이]
buildings.sort(key = lambda x: x[0]) # 인덱스 값으로 정렬
end_idx = buildings[-1][0] # 끝 인덱스
start_idx = buildings[0][0] # 첫 인덱스
mx_idx, mx = max(buildings, key = lambda x: x[1]) # 가장 큰 높이 인덱스, 높이

area = 0
top = buildings[0][1]
for n in range(len(buildings)):
    idx = buildings[n][0]
    if idx < mx_idx: # 최고점 직전까지 더 큰 값을 갱신하며 값 추가
        if idx >= top:
            top = buildings[n][1]
        for _ in range(buildings[n + 1][0] - idx):
            area += top

    elif idx == mx_idx: # 최고점 부분
        area += mx
        top = 0
        m_idx = n

    else: # 끝에서부터 최고점 직전까지 더 큰 값을 갱신하며 값 추가
        if buildings[len(buildings) - (n - m_idx)][1] >= top:
            top = buildings[len(buildings) - (n - m_idx)][1]
        for _ in range(buildings[len(buildings) - (n - m_idx)][0] - buildings[len(buildings) - (n + 1 - m_idx)][0]):
            area += top

print(area)










