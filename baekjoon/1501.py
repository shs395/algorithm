# 1501 - 영어 읽기
N = int(input())
dictionary = dict()
for _ in range(N):
    temp = input()
    if len(temp) == 1:
        temp_key = temp[0]
    else:
        temp_key = temp[0] + temp[-1]
    temp_key2 = ''.join(sorted(temp[1:-1]))
    if temp_key not in dictionary:
        dictionary[temp_key] = dict()
    if temp_key2 in dictionary[temp_key]:
        dictionary[temp_key][temp_key2] += 1
    else:
        dictionary[temp_key][temp_key2] = 1

M = int(input())
for _ in range(M):
    temp = input().split()
    temp_ans = 1
    for t in temp:
        # t = t.lower()
        if len(t) == 1:
            temp_key = t[0]
        else:
            temp_key = t[0] + t[-1]
        temp_key2 = ''.join(sorted(t[1:-1]))
        if temp_key not in dictionary:
            temp_ans = 0
            continue
        else:
            if temp_key2 not in dictionary[temp_key]:
                temp_ans = 0
                break
            else:
                temp_ans *= dictionary[temp_key][temp_key2]
    print(temp_ans)