# 1259 - 팰린드롬수
while True:
    temp = input()
    if temp == '0':
        break
    len_temp = len(temp)
    if len_temp % 2 == 0:
        if temp[:len_temp // 2] == temp[len_temp // 2:][::-1]:
            print('yes')
        else: 
            print('no')
    else:
        if temp[:len_temp // 2] == temp[len_temp // 2 + 1:][::-1]:
            print('yes')
        else:
            print('no')

        
