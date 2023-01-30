data = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}

def convert(n, x):
    result = ''
    while x > 0:
        if x % n >= 10:
            result = data[x % n] + result
        else:
            result = str(x % n) + result
        x //= n
    return result
        
def solution(n, t, m, p):
    answer = ''
    data = '0'
    idx = 1
    while True:
        if len(data) >= t * m:
            break
        data = data + convert(n, idx)
        idx += 1
        
    for i in range(len(data)):
        if i % m + 1 == p:
            answer = answer + data[i]
            if len(answer) == t:
                break
    return answer
