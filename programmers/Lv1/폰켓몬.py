def solution(nums):
    answer = 0
    arr = []
    for i in nums:
        if i not in arr:
            answer += 1
            arr.append(i)
        if answer >= len(nums) / 2:
            break
    
    return answer
