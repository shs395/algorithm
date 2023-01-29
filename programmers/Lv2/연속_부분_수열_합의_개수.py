def solution(elements):
    answer = set()
    new_arr = elements[:]
    new_arr.extend(elements)
    sum_arr = [0]
    for i in range(len(new_arr)):
        sum_arr.append(new_arr[i] + sum_arr[i])
        
    for i in range(1, len(elements) + 1):
        for j in range(i, len(sum_arr)):
            answer.add(sum_arr[j] - sum_arr[j - i])
    
    return len(answer)
