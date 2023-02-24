import sys
sys.stdin = open('input.txt')

def Dump(Dump_N, Box_H):
    Max_idx = 0 # 최댓값 인덱스
    Min_idx = 0 # 최솟값 인덱스

    for i in range(Dump_N):
        Max_idx = Box_H.index(max(Box_H)) # 최댓값 인덱스, 반복할 때마다 갱신
        Min_idx = Box_H.index(min(Box_H)) # 최솟값 인덱스, 반복할 때마다 갱신
        Box_H[Max_idx] -= 1  # 최댓값 -1
        Box_H[Min_idx] += 1 # 최솟값 +1

        if Box_H[Max_idx] - Box_H[Min_idx] <= 1: # 평탄화가 되었을 때
            return Box_H[Max_idx] - Box_H[Min_idx] # 차이 리턴
    
    return max(Box_H) - min(Box_H) # 차이 리턴


T = 10 # 테스트 케이스 수
Dump_Ns = [] # 덤프 횟수 리스트
Box_Hs = [] # 상자 높이값 리스트-리스트

for i in range(T):
    Dump_Ns.append(int(input()))
    Box_Hs.append(list(map(int, input().split())))

for i in range(T):
    Sub = Dump(Dump_Ns[i], Box_Hs[i]) # 인풋 그룹 하나씩 전달
    print(f'#{i + 1} {Sub}')