from collections import Counter
def solution(a):
    answer = 0
    for target, cnt in Counter(a).most_common():
        if cnt < answer:
            break

        t = 0
        nt = 0
        temp_cnt = 0
        for i in range(len(a)):
            if a[i] == target:
                t += 1
            else:
                nt += 1

            if t >= 1 and nt >= 1:
                t = 0
                nt = 0
                temp_cnt += 1

        answer = max(answer, temp_cnt * 2)

    return answer
