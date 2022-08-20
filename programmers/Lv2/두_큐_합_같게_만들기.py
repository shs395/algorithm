from collections import deque
def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)
    if (sum_queue1 + sum_queue2) % 2 != 0:
        return -1 
    
    while True:
        if sum_queue1 == sum_queue2:
            break
        elif sum_queue1 < sum_queue2:
            temp = queue2.popleft()
            queue1.append(temp)
            sum_queue1 += temp
            sum_queue2 -= temp
            answer += 1
        elif sum_queue1 > sum_queue2:
            temp = queue1.popleft()
            queue2.append(temp)
            sum_queue2 += temp
            sum_queue1 -= temp
            answer += 1
        if answer > 2 * (len(queue1) + len(queue2)):
            return -1
    return answer


