L, C = map(int, input().split())
letters = list(input().split())
vowels = ['a', 'e', 'i', 'o', 'u']

letters.sort()

def check(code):
    v_cnt, c_cnt = 0, 0

    for c in code:
        if c in vowels:
            v_cnt += 1
        else:
            c_cnt += 1

    if v_cnt >= 1 and c_cnt >= 2:
        return True
    else:
        return False


def backtracking(word):
    if len(word) == L:
        if check(word):
            print("".join(word))
        return

    for i in range(len(word), C):
        if word[-1] < letters[i]:
            backtracking(word + letters[i])

for i in range(C - L + 1):
    backtracking(letters[i])