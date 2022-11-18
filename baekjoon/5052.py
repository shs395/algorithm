# 5052 - 전화번호 목록
import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    tel = dict()
    n = int(input().rstrip())
    num_list = []
    flag = 0
    for _ in range(n):
        num_list.append(input().rstrip())
    num_list.sort(reverse=True, key=lambda x:len(x))
    for x in num_list:
        if x in tel:
            flag = 1
            break
        else:
            tel_temp = ''
            for t in x:
                tel_temp += t
                tel[tel_temp] = ''
    if flag == 1:
        print('NO')
    else:
        print('YES')

