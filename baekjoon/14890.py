# 14890 - 경사로
N, L = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

answer = 0
for i in range(N):
    start = arr[i][0]
    check = [False] * N
    j = 1
    flag = True
    while j < N:
        if arr[i][j] == start:
            j += 1
        elif start - arr[i][j] == 1:
            tmp = arr[i][j]
            tmp_flag = True
            for k in range(L):
                if j + k >= N:
                    tmp_flag = False
                    break
                if arr[i][j + k] == tmp:
                    check[j + k] = True
                    continue
                else:
                    tmp_flag = False
                    break
            if tmp_flag == False:
                flag = False
                break
            else:
                j = j + L
                start = tmp
        elif arr[i][j] - start == 1:
            tmp = arr[i][j] - 1
            tmp_flag = True
            for k in range(1, L + 1):
                if j - k < 0:
                    tmp_flag = False
                    break
                if arr[i][j - k] == tmp and check[j - k] == False:
                    continue
                else:
                    tmp_flag = False
                    break
            if tmp_flag == False:
                flag = False
                break
            else:
                start = arr[i][j]
                j = j + 1
                
        else:
            flag = False
            break
    if flag:
        answer += 1

for i in range(N):
    start = arr[0][i]
    check = [False] * N
    j = 1
    flag = True
    while j < N:
        if arr[j][i] == start:
            j += 1
        elif start - arr[j][i] == 1:
            tmp = arr[j][i]
            tmp_flag = True
            for k in range(L):
                if j + k >= N:
                    tmp_flag = False
                    break
                if arr[j + k][i] == tmp:
                    check[j + k] = True
                    continue
                else:
                    tmp_flag = False
                    break
            if tmp_flag == False:
                flag = False
                break
            else:
                j = j + L
                start = tmp
        elif arr[j][i] - start == 1:
            tmp = arr[j][i] - 1
            tmp_flag = True
            for k in range(1, L + 1):
                if j - k < 0:
                    tmp_flag = False
                    break
                if arr[j - k][i] == tmp and check[j - k] == False:
                    continue
                else:
                    tmp_flag = False
                    break
            if tmp_flag == False:
                flag = False
                break
            else:
                start = arr[j][i]
                j = j + 1
                
        else:
            flag = False
            break
    if flag:
        answer += 1

print(answer)