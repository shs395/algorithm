# 1107 - 리모컨
from itertools import product
N = int(input())
M = int(input())
buttons = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
available_channel_list = dict()
start = 100
count = abs(N - start)
if M != 0:
    broken_buttons = map(int, input().split())
    for b in broken_buttons:
        buttons.remove(b)

for i in range(1, 7):
    temp = list(product(buttons, repeat=i))
    for t in temp:
        available_channel_list[''.join(map(str, t))] = ''

if N == start:
    count = 0
else:
    for i in range(0, 999901):
        if str(start - i) in available_channel_list:
            count = min(count, len(str(start - i)) + abs(start - i - N))
        if str(start + i) in available_channel_list:
            count = min(count, len(str(start + i)) + abs(start + i - N))

print(count)