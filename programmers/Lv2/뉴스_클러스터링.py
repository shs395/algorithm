from collections import Counter
def x(s):
    if 97 <= ord(s) <= 122:
        return True
    else: 
        return False
def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    arr1 = []
    arr2 = []
    for i in range(len(str1) - 1):
        if x(str1[i]) and x(str1[i + 1]):
            arr1.append(str1[i:i + 2])
    for i in range(len(str2) - 1):
        if x(str2[i]) and x(str2[i + 1]):
            arr2.append(str2[i:i + 2])
    
    if len(arr1) == 0 and len(arr2) == 0:
        answer = 65536
    else:
        inter = len(arr1) - sum((Counter(arr1) - Counter(arr2)).values())
        union = sum((Counter(arr1) + Counter(arr2)).values()) - inter
        answer = (inter / union) * 65536
    
    return int(answer)
