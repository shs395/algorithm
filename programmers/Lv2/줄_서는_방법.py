import math
def solution(n, k):
    answer = []
    data = [i for i in range(1, n + 1)]
    k -= 1
    while n >= 1:
        divider = math.factorial(n - 1)
        answer.append(data[k // divider])
        data.remove(data[k // divider])
        k %= divider
        n -= 1
    return answer
