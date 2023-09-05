from itertools import permutations

def solution(user_id, banned_id):  
    def check(users, bans):
        for idx in range(len(bans)):
            if len(users[idx]) != len(bans[idx]):
                return False
            else:
                for l in range(len(users[idx])):
                    if bans[idx][l] == '*':
                        continue
                    if users[idx][l] != bans[idx][l]:
                        return False
        return True
    
    user_permutation = list(permutations(user_id, len(banned_id)))
    ban_set = []

    for users in user_permutation:
        if not check(users, banned_id):
            continue
        else:
            users = set(users)
            if users not in ban_set:
                ban_set.append(users)

    return len(ban_set)