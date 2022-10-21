# 10816 - 숫자 카드 2
from collections import Counter
input()
card_counter = Counter(list(map(int, input().split())))
input()
data = list(map(int, input().split()))

for i in data:
    print(card_counter[i], end=' ')