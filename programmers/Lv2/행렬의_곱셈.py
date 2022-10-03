def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp = [0 for _ in range(len(arr2[0]))]
        for j in range(len(arr1[i])):
            for k in range(len(arr2[j])):
                temp[k] += arr1[i][j] * arr2[j][k]
        answer.append(temp)
    return answer
