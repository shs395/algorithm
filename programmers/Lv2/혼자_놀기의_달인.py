def solution(cards):
    answer = 0
    visited = [False] * len(cards)
    boxes = []
    for i in range(len(cards)):
        temp = []
        idx = i
        while True:
            if visited[idx] == True:
                break
            visited[idx] = True
            temp.append(cards[idx])
            idx = cards[idx] - 1
        if len(temp) > 0:
            boxes.append(temp)
    
    if len(boxes) == 1:
        answer = 0
    else:
        boxes.sort(reverse=True, key=lambda x:len(x))
        answer = len(boxes[0]) * len(boxes[1])
    return answer
