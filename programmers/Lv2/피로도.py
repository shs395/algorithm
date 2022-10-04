from itertools import permutations
def solution(k, dungeons):
    answer = 0
    cases = list(permutations([i for i in range(len(dungeons))]))
    for case in cases:
        temp = 0
        temp_k = k
        for c in case:
            if dungeons[c][0] <= temp_k:
                temp_k -= dungeons[c][1]
                temp += 1
        answer = max(answer, temp)
    return answer
