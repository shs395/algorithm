# 2437 - 저울
N = int(input())
data = list(map(int, input().split()))
data.sort()

min_value = 1

for x in data:
    if x <= min_value:
        min_value += x
    else:
        break

print(min_value)