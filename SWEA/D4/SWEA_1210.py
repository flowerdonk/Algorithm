import sys
sys.stdin = open('input.txt')

def Ladder(arr):
    firstLine = []
    for x in range(len(arr[0])):
        if arr[0][x] == 1:
            firstLine.append(x) # 시작점 좌표 담기
    
    keep_x = 0
    keep_y = 0

    for start in firstLine: # 시작점 하나씩 반복
        keep_x = start # 시작점 저장
        y = 0
        x = firstLine.index(start) # 시작점 x 인덱스

        while x <= len(firstLine) - 1:
            if y == 99: # 마지막 줄
                if arr[y][firstLine[x]] == 2:
                    return keep_x
                else:
                    break
            #
            # if x == 0: # 첫번째 열
            #     if arr[y][firstLine[x] + 1] == 1:
            #         keep_y = y # y좌표 저장
            #         x += 1 # x 전 값으로
            #         y += 1
            #         continue # 다음 x좌표로
            #     else:
            #         y += 1
            #
            # elif x == len(firstLine) - 1: # 마지막 열
            #     if arr[y][firstLine[x] - 1] == 1: # 왼쪽 길
            #         keep_y = y # y좌표 저장
            #         x -= 1
            #         y += 1
            #         continue
            #     else:
            #         y += 1

            else:
                if x != len(firstLine) - 1 and arr[y][firstLine[x] + 1] == 1: # 오른쪽 길
                    keep_y = y # y좌표 저장
                    x += 1 # x 전 값으로 
                    y += 1
                    continue # 다음 x좌표로

                elif x != 0 and arr[y][firstLine[x] - 1] == 1: # 왼쪽 길
                    keep_y = y # y좌표 저장
                    x -= 1
                    y += 1
                    continue
                
                else:
                    y += 1
            
    return -1


result = []
for _ in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result.append(Ladder(arr))

for i in range(10):
    print(f'#{i + 1} {result[i]}')