from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    arr = defaultdict(int)
    for order in orders:
        order = list(order)
        order.sort()
        order = ''.join(order)
        for i in range(2, len(order) + 1):
            temp_list = list(map(''.join, combinations(order, i)))
            for temp in temp_list:
                arr[temp] += 1
                
    for c in course:
        temp_max = -1
        for key in arr.keys():
            if len(key) == c:
                if arr[key] < 2:
                    continue
                temp_max = max(temp_max, arr[key])
                
        if temp_max == -1:
            continue
            
        for key in arr.keys():
            if len(key) == c:
                if arr[key] == temp_max:
                    answer.append(key)
    
    answer.sort()
    return answer
