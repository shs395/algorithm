# 1759 - 암호 만들기
from itertools import combinations
L, C = map(int, input().split())
data = list(input().split())
x = ['a', 'e', 'i', 'o', 'u']
data.sort()
for i in list(combinations(data, L)):
    cnt_1 = 0
    cnt_2 = 0
    for j in i:
        if j in x:
            cnt_1 += 1
        else:
            cnt_2 += 1
    if cnt_1 >= 1 and cnt_2 >= 2:
        print(''.join(i))
