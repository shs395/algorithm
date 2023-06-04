# 1972 - 놀라운 문자열
while True:
    x = input()
    if x == '*':
        break
    flag = True
    for i in range(len(x) - 1):
        data = dict()
        for j in range(len(x) - i - 1):
            tmp = x[j] + x[j + i + 1]
            if tmp in data:
                flag = False
                break
            else:
                data[tmp] = 1
        if flag == False:
            break
    if flag:
        print(f'{x} is surprising.')
    else:
        print(f'{x} is NOT surprising.')
