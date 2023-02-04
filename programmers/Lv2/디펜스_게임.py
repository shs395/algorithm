def x(n, k, enemy):
    enemy.sort(reverse=True)
    if k >= len(enemy):
        return True
    
    if sum(enemy[k:]) <= n:
        return True
    else:
        return False
        
    
def solution(n, k, enemy):
    answer = 0
    start = 0
    end = len(enemy)
    while start <= end:
        mid = (start + end) // 2
        if x(n, k, enemy[:mid]) == True:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    return answer
