# 1013 - Contact
# fullmatch 를 사용하자
import re
T = int(input())
a = re.compile('(100+1+|01)+')
for _ in range(T):
    s = input()
    result = a.fullmatch(s)
    if result:
        print('YES')
    else:
        print('NO')
