def check(arr, start, end):
    if end[0] - start[0] == 1 or end[1] - start[1] == 1:
        return 
    flag = True
    s = arr[start[0]][start[1]] 
    for i in range(start[0], end[0]):
        for j in range(start[1], end[1]):
            if s != arr[i][j]:
                flag = False
                break
    
    if flag:
        for i in range(start[0], end[0]):
            for j in range(start[1], end[1]):
                arr[i][j] = -1
        arr[start[0]][start[1]] = s
    else:
        check(arr, (start[0], start[1]), ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2))
        check(arr, ((start[0] + end[0]) // 2, start[1]), (end[0], (start[1] + end[1]) // 2))
        check(arr, (start[0], (start[1] + end[1]) // 2), ((start[0] + end[0]) // 2, end[1]))
        check(arr, ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2), (end[0], end[1]))
                
def solution(arr):
    answer = [0, 0]
    check(arr, (0, 0), (len(arr), len(arr)))
    for x in arr:
        for y in x:
            if y == 0:
                answer[0] += 1
            elif y == 1:
                answer[1] += 1
    return answer
