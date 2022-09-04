def solution(s):
    len_s = len(s)
    for i in range(len_s, 0, -1):
        for j in range(len_s - i + 1):
            temp = s[j:j + i]
            if temp == temp[::-1]:
                return i
