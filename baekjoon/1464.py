# 1464 - 뒤집기 3
S = input()
for i in range(1, len(S)):
    if S[i] > S[i - 1]:
        S = S[i] + S[:i] + S[i + 1:]

print(S[::-1])
