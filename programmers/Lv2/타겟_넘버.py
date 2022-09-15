def solution(numbers, target):
    answer = 0
    data = [-1, 1]
    def dfs(idx, result, params):
        result += params * numbers[idx]
        if idx == len(numbers) - 1:
            if result == target:
                nonlocal answer 
                answer += 1
        else:
            dfs(idx + 1, result, 1)
            dfs(idx + 1, result, -1)
            
    dfs(0, 0, 1)
    dfs(0, 0, -1)
        
    return answer


