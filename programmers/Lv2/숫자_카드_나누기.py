import math
def solution(arrayA, arrayB):
    answer = 0
    arrayA.sort()
    arrayB.sort()
    a_gcd = arrayA[0]
    b_gcd = arrayB[0]
    a_list = []
    b_list = []
    
    for x in arrayA[1:]:
        a_gcd = math.gcd(x, a_gcd)
        
    for x in arrayB[1:]:
        b_gcd = math.gcd(x, b_gcd)
    
    for i in range(1, a_gcd + 1):
        if a_gcd % i == 0:
            a_list.append(i)
    
    for i in range(1, b_gcd + 1):
        if b_gcd % i == 0:
            b_list.append(i)
    
    a_list.sort(reverse=True)
    b_list.sort(reverse=True)
    
    for x in a_list:
        flag = True
        for y in arrayB:
            if x <= y and y % x == 0:
                flag = False
                break
        
        if flag == True:
            answer = max(answer, x)
            break
            
    for x in b_list:
        flag = True
        for y in arrayA:
            if x <= y and y % x == 0:
                flag = False
                break
        
        if flag == True:
            answer = max(answer, x)
            break
            
    return answer
