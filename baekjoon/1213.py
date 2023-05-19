# 1213 - 팰린드롬 만들기
data = list(input())

cnt = dict()

for x in data:
    if x not in cnt:
        cnt[x] = 1
    else:
        cnt[x] += 1

tmp = 0
for x in cnt.values():
    if x % 2 == 1:
        tmp += 1

answer = ''
r = ''
if len(data) % 2 == 1 and tmp > 1:
    print("I'm Sorry Hansoo")
elif len(data) % 2 == 0 and tmp > 0:
    print("I'm Sorry Hansoo")
else:
    for x in sorted(cnt.keys()):
        answer += x * (cnt[x] // 2)
        cnt[x] %= 2
        if cnt[x] % 2 == 1:
            r = x
    answer = answer + r + answer[::-1]
    print(answer)



