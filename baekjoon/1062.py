# 1062 - 가르침
from itertools import combinations

N, K = map(int, input().split())
answer = 0
words = [0] * N
s = ['a', 'n', 't', 'i', 'c']

for i in range(N):
    word = list(input())[4:-4]
    for c in word:
        words[i] |= (1 << ord(c) - ord('a'))

if K >= 5:
    data = 'bdefghjklmopqrsuvwxyz'
    all_case = list(combinations(list(data), K - 5))
    for case in all_case:
        tmp = 0
        for c in s:
            tmp |= (1 << ord(c) - ord('a'))
        for c in case:
            tmp |= (1 << ord(c) - ord('a'))

        cnt = 0
        for i in range(len(words)):
            if words[i] & tmp == words[i]:
                cnt += 1
        
        if cnt > answer:
            answer = cnt

print(answer)