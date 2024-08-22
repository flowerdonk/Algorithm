N = int(input())                        # 사진틀 수
R = int(input())                        # 전체 학생 총 추천 횟수
nums = list(map(int, input().split()))  # 추천받은 학생 번호 (순서)

pics = [[R + 1, R + 1] for _ in range(max(nums) + 1)]       # pics[학생 번호] = (추천 횟수, 게시된 시간)
cnt = 0                                 # 사진 게시 수
temp = 1
for num in nums:
    if cnt >= N and pics[num][0] == R + 1:
        # 최솟값 찾기
        min_reco = min(pics, key=lambda x:x[0])[0]
        # 게시된 시간이 가장 오래된 학생 번호 찾기
        old_num = min((i for i, v in enumerate(pics) if v[0] == min_reco), key=lambda x: pics[x][1])
        pics[old_num] = [R + 1, R + 1]

    if pics[num][0] == R + 1:
        pics[num][0] = 1
    else:
        pics[num][0] += 1
    if pics[num][1] == R + 1:
        pics[num][1] = temp
        cnt += 1
    temp += 1

ans = list((i for i, v in enumerate(pics) if v[0] != R + 1))
print(*ans)
