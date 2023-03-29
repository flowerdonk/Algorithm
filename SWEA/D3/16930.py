import sys
sys.stdin = open('input.txt')

def merge_sort(data):
    global cnt
    if len(data) < 2:
        return data

    middle = len(data) // 2
    low = merge_sort(data[:middle])
    high = merge_sort(data[middle:])

    if low[-1] > high[-1]:
        cnt += 1

    merged_data = []
    low_idx, high_idx = 0, 0
    while low_idx < len(low) and high_idx < len(high):
        if low[low_idx] < high[high_idx]:
            merged_data.append(low[low_idx])
            low_idx += 1
        else:
            merged_data.append(high[high_idx])
            high_idx += 1

    merged_data += low[low_idx:]
    merged_data += high[high_idx:]

    return merged_data

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    cnt = 0
    merged_data = merge_sort(data)
    print(merged_data)
    print(f'#{tc} {merged_data[N//2]} {cnt}')
