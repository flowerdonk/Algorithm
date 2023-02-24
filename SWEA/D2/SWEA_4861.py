import sys
sys.stdin = open('input.txt')

def palindrome(N, M, Tcase):
    result = ''
    Ans = []
    for i in range(N):  # 가로 세로 동시 판별
        cnt = 0
        for j in range(N - M + 1):  # 가로 : 한 줄에 길이가 될 때 까지만
            for r in range(M // 2):  # 기준점 j부터 M 이후 글자에서 안으로
                if Tcase[i][j + r] == Tcase[i][j + M - r - 1]:  # 기준점 j부터 M 이후 글자
                    cnt += 1
                else:
                    cnt = 0
                    break
            if cnt == M // 2:
                for s in range(M):
                    result += Tcase[i][s + j]
                # result = Tcase[i][j: j + M]
                Ans.append(str(result))
                result = ''
                # return result
        cnt = 0
        for k in range(N - M + 1):  # 세로 : 한 줄에 길이가 될 때 까지만
            for r in range(M // 2):  # 기준점 j부터 M 이후 글자에서 안으로
                if Tcase[k + r][i] == Tcase[k + M - r - 1][i]:  # 기준점 j부터 M 이후 글자
                    cnt += 1
                else:
                    cnt = 0
                    break
            if cnt == M // 2:
                for l in range(M):
                    result += Tcase[l + k][i]
                Ans.append(str(result))
                result = ''
                # return result
    return Ans

T = int(input())
for tc in range(T):
    N, M = map(int, input().split()) # N : 글자판 크기, M : 길이
    Tcase = [input() for _ in range(N)]
    Ans = palindrome(N, M, Tcase)
    for j in range(len(Ans)):
        print(f'#{tc + 1}', Ans[j])
