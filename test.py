from sys import stdin
stdin = open('input.txt')
'''
끝나는 시간이 이른 순으로 정렬 -> 끝나는 시간이 같을 때를 고려해 시작 시간이 이른 순으로 한번 더 정렬([1, 2], [2, 2])
시간 순으로 정렬했으니 데이터를 순회하며 그 다음 데이터가 이전 데이터의 끝나는 시간 이후인지를 확인 후 갱신
'''
N = int(stdin.readline()) # 회의 수
data = [list(map(int, stdin.readline().split())) for _ in range(N)] # [시작, 끝]
data.sort(key= lambda x: (x[1], x[0])) # 튜플로 여러 인자 전달 시 해당 순서대로 정렬

end = data[0][1] # 가장 빨리 끝나는 것이 첫 번째 회의
cnt = 1 # 시작 1 -> 첫 원소 포함
for s, e in data[1:]: # 두 번째 부터
    if s >= end:
        end = e
        cnt += 1

print(cnt)