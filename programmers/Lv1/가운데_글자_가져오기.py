def solution(s):
    len_s = len(s)
    if len_s % 2 == 0:
        return s[int(len_s / 2) - 1 : int(len_s / 2) + 1]
    else:
        return s[int(len_s // 2)]
