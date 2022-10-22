# 1074 - Z
N, r, c = map(int, input().split())
length = pow(2, N)
start = 1
end = pow(2, N) * pow(2, N)
ans = 0
while True:
    if length == 2:
        if r == 0 and c == 0:
            ans = start
        elif r == 0 and c == 1:
            ans = start + 1
        elif r == 1 and c == 0:
            ans = start + 2
        else:
            ans = start + 3
        break
    temp = length * length // 4
    if r < length // 2 and c < length // 2:
        end = start + temp - 1
    elif r < length // 2 and c >= length // 2:
        start = start + temp
        end = start + (2 * temp) - 1
    elif r >= length // 2 and c < length // 2:
        start = start + (2 * temp)
        end = start + (3 * temp) - 1
    else:
        start = start + (3 * temp)
    
    length = length // 2
    r = r % length
    c = c % length 

print(ans - 1)