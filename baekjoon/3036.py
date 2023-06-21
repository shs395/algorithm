# 3036 - 링
import math
N = int(input())
data = list(map(int, input().split()))

s = data[0]
for x in data[1:]:
    print(f'{s//math.gcd(s, x)}/{x//math.gcd(s, x)}')
