from itertools import product

def solution(word):
    answer = 0
    data = []
    for i in range(1, 6):
        data.extend(list(map(''.join, product(['A','E','I','O','U'], repeat = i))))
    
    data.sort()
    
    return data.index(word) + 1
