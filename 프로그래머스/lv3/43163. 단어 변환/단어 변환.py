from collections import deque

def solution(begin, target, words):
    answer = 0
    N = len(words)
    word_len = len(begin)
    visited = [False] * N
    
    q = deque()
    q.append((begin, 0))
    
    while q:
        word, cnt = q.popleft()
        
        if word == target:
            answer = cnt
    
        for n in range(N):
            if not visited[n]:
                temp = 0
                for l in range(word_len):
                    if word[l] != words[n][l]:
                        temp += 1
                if temp == 1:
                    q.append((words[n], cnt + 1))
                    visited[n] = True
    
    return answer