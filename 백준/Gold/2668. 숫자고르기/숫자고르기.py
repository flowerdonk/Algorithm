import sys

N = int(input())
nums = [0]
result = set()
for _ in range(N):
    nums.append(int(input()))

def dfs(idx, start):
    visited[idx] = True
    next_idx = nums[idx]
    if visited[next_idx] and next_idx == start:
        result.update({i for i, val in enumerate(visited) if val})
        return
    elif not visited[next_idx]:
        dfs(next_idx, start)

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    dfs(i, i)

print(len(result))
result_list = list(result)
result_list.sort()
for i in result_list:
    print(i)