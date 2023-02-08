def solution(weights):
    answer = 0
    data = dict()
    for weight in weights:
        if weight not in data:
            data[weight] = 1
        else:
            data[weight] += 1
            
    weights = list(set(weights))
    weights.sort()
    
    for weight in weights:
        if data[weight] > 1:
            answer += (data[weight] * (data[weight] - 1)) // 2
        if weight / 2 * 3 in data:
            answer += data[weight] * data[weight / 2 * 3]
        if weight / 2 * 4 in data:
            answer += data[weight] * data[weight / 2 * 4]
        if weight / 3 * 4 in data:
            answer += data[weight] * data[weight / 3 * 4]
    return answer

