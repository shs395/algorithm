# 7490 - 0 만들기
# eval() 함수로 식을 엄청나게 단축시킬 수 있었다.
T = int(input())

def func(data, value, num, end):
    if num == end + 1:
        if eval(data.replace(' ', '')) == 0:
            print(data)
        return 
    func(data + ' ' + str(num), value + 10 * (num - 1) + num, num + 1, end)
    func(data + '+' + str(num), value + num, num + 1, end)
    func(data + '-' + str(num), value - num, num + 1, end)
    

for _ in range(T):
    N = int(input())
    func('1', 1, 2, N)
    print()