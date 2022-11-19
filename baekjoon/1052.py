# 1052 - 물병
N, K = map(int, input().split())

def a(num):
    cnt = 0
    while num > 1:
        num //= 2
        cnt += 1
    return pow(2, cnt)

stack = []
ans = 0
while N > 0:
    temp = a(N)
    N -= temp
    stack.append(temp)

while True:
    if len(stack) > K:
        need = stack[-2] - stack[-1]
        stack[-1] += need
        ans += need
        while True:
            if len(stack) == 1 or stack[-2] != stack[-1]:
                break
            else:
                temp = stack.pop()
                stack[-1] += temp
    else:
        break

print(ans)
