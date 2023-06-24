def solution(triangle):
    l = len(triangle[-1])
    dp = [[0] * x for x in range(1, l + 1)]
    dp[0][0] = triangle[0][0]
    
    for i in range(l):
        for j in range(i + 1):
            if j == 0:
                if i == 0:
                    break
                else:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
    
    return max(dp[-1])