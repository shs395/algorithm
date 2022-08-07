def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp = ''
        temp_arr1 = bin(arr1[i])[2:].zfill(n)
        temp_arr2 = bin(arr2[i])[2:].zfill(n)
        for j in range(n):
            if temp_arr1[j] == '1' or temp_arr2[j] == '1':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
    return answer
