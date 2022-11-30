def solution(stones, k):
    answer = 0
    start = 1
    end = 200000000
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for stone in stones:
            if stone < mid:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid
    return answer
