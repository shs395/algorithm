def solution(n):
    fib = [0] * 100001
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n] % 1234567
