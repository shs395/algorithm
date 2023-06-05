# 1254 - 팰린드롬 만들기
S = input()

answer = 0
for i in range(len(S)):
    if S[i:] == S[i:][::-1]:
        answer = len(S) + i
        break

print(answer)

