# 1431 - 시리얼 번호
N = int(input())
data = []
for _ in range(N):
    tmp = input()
    cnt = 0
    for x in tmp:
        if x.isdigit():
            cnt += int(x)
    data.append((tmp, cnt))
    
data.sort()
data.sort(key=lambda x:x[1])
data.sort(key=lambda x:len(x[0]))

for x in data:
    print(x[0])
