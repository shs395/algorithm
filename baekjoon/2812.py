# 2812 - 크게 만들기
N, K = map(int, input().split())
num = input()
stack = []
    
for idx in range(N):
    x = int(num[idx])
    if len(stack) == 0:
        stack.append(x)
    else:
        if x > stack[-1]:
            while True:
                if len(stack) == 0 or K == 0:
                    stack.append(x)
                    break
                if x > stack[-1]:
                    stack.pop()
                    K -= 1
                else:
                    stack.append(x)
                    break
        else:
            stack.append(x)

if K > 0:
    for _ in range(K):
        stack.pop()


print(int(''.join(map(str, stack))))