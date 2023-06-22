# 2331 - 반복수열
A, P = map(int, input().split())
data = [A]
C = dict()
C[A] = 1
answer = 0

idx = 0
while True:
    tmp = 0
    for x in list(str(data[idx])):
        tmp += pow(int(x), P)
    if tmp in C:
        answer = C[tmp] - 1
        break
    else:
        data.append(tmp)
        idx += 1
        C[tmp] = idx + 1
        
print(answer)