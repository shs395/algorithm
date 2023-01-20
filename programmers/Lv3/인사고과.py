from collections import Counter
def solution(scores):
    answer = 0
    wanho = scores[0]
    new_scores = []
    
    for i in range(1, len(scores)):
        if wanho[0] < scores[i][0] and wanho[1] < scores[i][1]:
            return -1
    
    scores.sort(key=lambda x:x[1])
    max_1 = scores[0][1]
    scores.sort(reverse=True, key=lambda x:x[0])

    for i in range(len(scores)):
        if scores[i][1] >= max_1:
            new_scores.append(scores[i][0] + scores[i][1])
            max_1 = scores[i][1]
            
    for x in Counter(new_scores).most_common():
        if x[0] > wanho[0] + wanho[1]:
            answer += x[1]

    return answer + 1

