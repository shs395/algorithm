import math

def isPrime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return 0 
    return 1 

def solution(nums):
    answer = 0
        
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                temp = nums[i] + nums[j] + nums[k]
                answer += isPrime(temp)
    return answer
