def solution(a):
    len_a = len(a)
    answer = len_a
    left = [0] * len_a
    right = [0] * len_a
    left[0] = a[0]
    right[-1] = a[-1]
    for i in range(1, len_a):
        if a[i] < left[i - 1]:
            left[i] = a[i]
        else:
            left[i] = left[i - 1]
        
        if a[len_a - 1 - i] < right[len_a - i]:
            right[len_a - 1 - i] = a[len_a - 1 - i]
        else:
            right[len_a - 1 - i] = right[len_a - i]
    
    for i in range(len_a):
        if i == 0 or i == len_a - 1:
            continue
        else:
            if left[i - 1] < a[i] and right[i + 1] < a[i]:
                answer -= 1

    return answer
