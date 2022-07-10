def solution(s):
    answer = ''
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    temp = ''
    for i in s:
        if ord(i) >= 48 and ord(i) <= 57:
            answer += i
        else:
            temp += i
            if temp in arr:
                answer += str(arr.index(temp))
                temp = ''
    return int(answer)




