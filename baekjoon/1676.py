# 1676 - 팩토리얼 0의 개수
import math
N = int(input())
a = str(math.factorial(N))[::-1]
count = 0
for i in a:
    if i != '0':
        break
    else:
        count += 1
print(count)