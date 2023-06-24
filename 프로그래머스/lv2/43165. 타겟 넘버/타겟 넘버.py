def solution(numbers, target):
    answer = [0]
    def dfs(idx, rst, numbers, target):
        if idx == len(numbers):
            if rst == target:
                answer[0] += 1
            return

        dfs(idx + 1, rst - numbers[idx], numbers, target)
        dfs(idx + 1, rst + numbers[idx], numbers, target)
        return
    dfs(0, 0, numbers, target)
    return answer[0]
    
    