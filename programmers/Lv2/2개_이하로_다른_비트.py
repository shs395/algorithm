def binary(x):
    result = ''
    while x > 1:
        result = str(x % 2) + result
        x //= 2
    result = str(x) + result
    return result

def change(x):
    flag = True
    one_idx = -1
    for i in range(len(x) - 1, -1, -1):
        if x[i] == '1':
            one_idx = i
        elif x[i] == '0':
            if one_idx != -1:
                x = x[:i] + '1' + x[i + 1:]
                x = x[:one_idx] + '0' + x[one_idx + 1:]
            else:
                x = x[:i] + '1' + x[i + 1:]
            flag = False
            break
        
    if flag:
        x = '10' + x[1:]
    return x

def decimal(x):
    idx = 1
    result = 0
    for i in range(len(x) - 1, -1, -1):
        result += int(x[i]) * idx
        idx *= 2
    return result

def solution(numbers):
    answer = []
    for number in numbers:
        b_number = binary(number)
        b_number = change(b_number)
        answer.append(decimal(b_number))
        
        
    return answer
