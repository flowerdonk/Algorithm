l, w, h = map(int, input().split()) # 박스 크기 length, width, height
N = int(input()) # 큐브 종류 개수
cubes = [] # [큐브 한 변의 길이 2의 지수, 해당 큐브 개수]
for n in range(N):
    idx, val = map(int, input().split())
    cubes.append([2 ** idx, val])
cubes.sort(reverse=True) # 큰 수부터 채우기 위해서

ans = 0 # 큐브 개수
total = 0 # 큐브가 찬 영역 (큐브 단위 기준, 큐브 한 변의 길이가 달라질 수록 그 단위대로 증가)
for L, N in cubes: # 한 변의 길이, 개수
    total *= 8 # 전 큐브 1개 = 다음 큐브 8개 ex) 4 * 4 * 4 = (2 * 2 * 2) * 8

    fill = (l // L) * (w // L) * (h // L) - total # 큐브로 전체 채웠을 때 개수 - 전에 이미 채운 부분
    fill = N if N <= fill else fill # 큐브 개수보다 크면 큐브 개수만큼만 채우기

    total += fill # 영역에 추가
    ans += fill # 개수에 추가

if total < l * w * h: # 채워진 영역이 총 영역보다 작으면 다 못채운 것
    print(-1)
else:
    print(ans)