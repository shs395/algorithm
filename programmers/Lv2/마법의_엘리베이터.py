answer = int(1e9)

def dfs(idx, arr, ans):
    global answer
    if idx == len(arr):
        answer = min(ans, answer)
        return 
    
    if arr[idx] >= 10:
        if idx + 1 < len(arr):
            arr[idx + 1] += 1
        else:
            ans += 1
        arr[idx] = 0
        
    dfs(idx + 1, arr[:], ans + arr[idx])
    
    if idx + 1 < len(arr):
        arr[idx + 1] += 1
    else:
        ans += 1
        
    dfs(idx + 1, arr, ans + (10 - arr[idx]))
    
def solution(storey):
    x = list(map(int, str(storey)))
    x.reverse()
    dfs(0, x, 0)
    
    return answer
