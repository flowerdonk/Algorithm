import sys
sys.setrecursionlimit(10**9)

def solution(n, computers):
    answer = 0
    connection = [False] * n
    
    def dfs(idx, n):
        connection[idx] = True
        for com in range(n):
            if idx != com and computers[idx][com] == 1 and not connection[com]:
                dfs(com, n)
    
    for idx in range(n):
        if not connection[idx]:
            dfs(idx, n)
            answer += 1

    return answer