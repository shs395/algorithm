# 17298 - 오큰수
A = int(input())
data = list(map(int, input().split()))
stack = []
answer = [-1] * len(data)

for i in range(len(data)):
    if len(stack) == 0:
        stack.append((data[i], i))
    else:
        while True:
            if len(stack) == 0 or stack[-1][0] >= data[i]:
                break
            elif stack[-1][0] < data[i]:
                _, idx = stack.pop()
                answer[idx] = data[i]
        stack.append((data[i], i))

print(*answer)
