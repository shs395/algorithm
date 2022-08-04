def solution(n):
    temp = str(bin(n)).count('1')
    while True:
        n += 1
        if str(bin(n)).count('1') == temp:
            break
    return n
