# 1043 - 거짓말
N, M = map(int, input().split())
party_list = []
true_list = list(map(int, input().split()))
true_set = set(true_list[1:])
answer = 0

for _ in range(M):
    temp_party = list(map(int, input().split()))
    party_list.append(set(temp_party[1:]))
    for p in temp_party[1:]:
        if p in true_set:
            true_set = true_set.union(set(temp_party[1:]))
            break

for _ in range(M - 1):
    for party in party_list:
        for p in party:
            if p in true_set:
                true_set = true_set.union(set(party))
                break

for party in party_list:
    if len(party & true_set) == 0:
        answer += 1

print(answer)

