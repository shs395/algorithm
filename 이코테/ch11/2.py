# 2 - 곱하기 혹은 더하기
s = list(input())
answer = int(s[0])
if len(s) > 1:
    for c in s[1:]:
        if answer * int(c) > answer + int(c):
            answer *= int(c)
        else:
            answer += int(c)

print(answer)