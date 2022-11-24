def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    start = 0
    end = distance
    while start <= end:
        mid = (start + end) // 2
        now = 0
        cnt = 0
        for rock in rocks:
            if rock - now < mid:
                cnt += 1
            else:
                now = rock
        if cnt > n:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid
        
        
    return answer
