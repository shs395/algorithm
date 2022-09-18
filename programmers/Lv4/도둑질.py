def solution(money):
    answer = 0
    money.insert(0, 0)
    temp = money[:]
    
    money[1] = 0
    for i in range(2, len(money)):
        money[i] = max(money[i - 1], money[i - 2] + money[i])
    
    for i in range(2, len(temp) - 1):
        temp[i] = max(temp[i - 1], temp[i - 2] + temp[i])
        
    return max(max(money), max(temp))
