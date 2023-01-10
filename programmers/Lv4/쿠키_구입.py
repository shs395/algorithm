def solution(cookie):
    answer = 0
    sum_list = [0]
    for c in cookie:
        sum_list.append(sum_list[-1] + c)
    
    for m in range(len(cookie) - 1):
        left_idx = 0
        right_idx = len(cookie)
        while left_idx <= m and right_idx >= m + 1:
            left_sum = sum_list[m + 1] - sum_list[left_idx]
            right_sum = sum_list[right_idx] - sum_list[m + 1]
            if left_sum == right_sum:
                answer = max(answer, left_sum)
                left_idx += 1
                right_idx -= 1
            elif left_sum > right_sum:
                left_idx += 1
            elif left_sum < right_sum:
                right_idx -= 1
            
    return answer

