# 2671 - 잠수함식별
import re
a = re.compile('(100+1+|01)+')
data = input()
if a.fullmatch(data):
    print('SUBMARINE')
else:
    print('NOISE')