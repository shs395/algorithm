import math

def lcm(x, y):
    return x * y // math.gcd(x,y)

def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        arr[i] = lcm(arr[i - 1], arr[i])
    
    return arr[-1]
