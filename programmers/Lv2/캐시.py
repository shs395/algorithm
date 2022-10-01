from collections import deque
def solution(cacheSize, cities):
    answer = 0
    queue = deque([])
    for city in cities:
        city_low = city.lower()
        if cacheSize == 0:
            answer = len(cities) * 5
            break
        if len(queue) < cacheSize:
            if city_low in queue:
                queue.remove(city_low)
                answer += 1
            else:
                answer += 5
            queue.append(city_low)
        else:
            if city_low in queue:
                queue.remove(city_low)
                answer += 1
            else:
                queue.popleft()
                answer += 5
            queue.append(city_low)
        
    return answer
