def binary_search(start, end, food_times, k):
    result = [0, 0]
    while start <= end:
        mid = (start + end) // 2
        temp = 0
        for food in food_times:
            if food >= mid:
                temp += mid
            else:
                temp += food
        
        if temp <= k:
            result = [mid, temp]
            start = mid + 1
        else:
            end = mid - 1
    return result
            
def solution(food_times, k):
    answer = 0
    max_food = max(food_times)
    cycle, eat_amount = binary_search(0, max_food, food_times, k)
    eat_left = k - eat_amount
    
    if cycle >= max_food:
        return -1
    
    for i in range(len(food_times)):
        if eat_left == 0 and food_times[i] > cycle:
            answer = i + 1
            break
        if food_times[i] > cycle:
            eat_left -= 1
        
    return answer

