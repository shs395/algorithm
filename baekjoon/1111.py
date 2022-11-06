# 1111 - IQ Test
N = int(input())
data = list(map(int, input().split()))
answer = 0
answer_set = set()
if N == 1:
    print('A')
elif N == 2 and len(set(data)) == 1:
    print(data[0])
elif N == 2:
    print('A')
else:
    if data[1] - data[0] == 0:
        a = 1
        b = 0
    else:
        a = (data[2] - data[1]) // (data[1] - data[0])
        b = data[1] - data[0] * a
    answer = data[-1] * a + b
    for i in range(len(data) - 1):
        if data[i] * a + b != data[i + 1]:
            answer = 'B'
            break
    print(answer)
        

