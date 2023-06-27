# 1059 - 좋은 구간
L = int(input())
data = list(map(int, input().split()))
data.sort()
n = int(input())
answer = 0
flag = False
left = 0
right = 0

for i in range(len(data)):
    if data[i] == n:
        answer = -1
        break
    if not flag and data[i] > n:
        flag = True
        if i == 0:
            left = -1
        else:
            left = data[i - 1] + 1
    if flag and data[i] > n:
        right = data[i] - 1
        break

if answer == -1 or right == 0 or L == 1:
    print(0)
elif left == -1:
    for x in range(1, right + 1):
        if x > n:
            break
        if x == n:
            answer += right - x 
        elif x < n:
            answer += right - n + 1
    print(answer)
else:
    for x in range(left, right + 1):
        if x > n:
            break
        if x == n:
            answer += right - x 
        elif x < n:
            answer += right - n + 1

    print(answer)