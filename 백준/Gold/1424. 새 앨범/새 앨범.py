N = int(input())    # 노래 개수
L = int(input())    # 노래 길이
C = int(input())    # CD 용량
ans = 0

# 한 시디 노래 개수는 13의 배수 X
# 노래 사이 1초 간격

song_count_per_cd = C // (L + 1)
if C % (L + 1) == L:            # 마지막에 1곡 더 추가 가능
    song_count_per_cd += 1
if not song_count_per_cd % 13:  # 13 배수일 경우
    song_count_per_cd -= 1

if song_count_per_cd > N:       # 한 cd에 모두 수용 가능
    ans = 1 if N % 13 else 2  # 13의 배수면 CD 추가
else:
    ans = N // song_count_per_cd
    remain = N % song_count_per_cd

    if remain > 0:
        if remain % 13 == 0:
            if song_count_per_cd > 13 and (song_count_per_cd - 1) % 13:
                ans += 1
            else:
                ans += 2
        else:
            ans += 1

print(ans)