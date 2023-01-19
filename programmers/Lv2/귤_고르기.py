from collections import Counter
def solution(k, tangerine):
    answer = 0
    for x in Counter(tangerine).most_common():
        if k <= 0:
            break
        k -= x[1]
        answer += 1
    return answer
