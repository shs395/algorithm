from collections import deque, Counter
def solution(want, number, discount):
    answer = 0
    temp = []
    for i in range(len(number)):
        for j in range(number[i]):
            temp.append(want[i])
            
    queue = deque(discount[:10])
    want_counter = Counter(temp)
    if want_counter - Counter(queue) == Counter():
            answer += 1
            
    for i in range(len(discount) - 10):
        queue.popleft()
        queue.append(discount[i + 10])
        if want_counter - Counter(queue) == Counter():
            answer += 1
        
    return answer
