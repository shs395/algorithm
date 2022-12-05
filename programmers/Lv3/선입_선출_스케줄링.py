def solution(n, cores):
    answer = 0
    start = 1
    end = 500000000
    idx = 0
    while start <= end:
        mid = (start + end) // 2
        temp_sum = 0
        for core in cores:
            temp_sum += 1 + (mid - 1) // core
            if temp_sum > n:
                break
        
        if temp_sum >= n:
            end = mid - 1
            idx = mid
        elif temp_sum < n:
            start = mid + 1
            
    if idx == 1:
        return cores[n - 1]
    else:
        temp = 0
        for core in cores:
            temp += 1 + (idx - 2) // core
        
        temp_count = n - temp
        for i in range(len(cores)):
            if (idx - 1) % cores[i] == 0:
                temp_count -= 1
                if temp_count == 0:
                    return i + 1
            
