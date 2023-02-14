def solution(order):
    answer = 0
    stack = []
    idx = 1
    for x in order:
        if x > idx:
            while idx != x:
                stack.append(idx)
                idx += 1
            idx += 1
            answer += 1
        elif x == idx:
            answer += 1
            idx += 1
        elif x < idx:
            if stack[-1] == x:
                stack.pop()
                answer += 1
            else:
                break
    return answer
