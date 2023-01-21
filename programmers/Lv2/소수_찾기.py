import math
from itertools import permutations

def isPrime(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True		
                    
def solution(numbers):
    answer = 0
    dataset = []
    for i in range(1, len(numbers) + 1):
        dataset.extend(list(set(permutations(map(int, list(numbers)), i))))
    for x in dataset:
        temp = ''
        if x[0] == 1 and len(x) == 1:
            continue
        if x[0] == 0:
            continue
        for y in x:
            temp += str(y)
        temp = int(temp)
        if isPrime(temp) == True:
            answer += 1
    return answer
