# 1474 - 밑 줄
N, M = map(int, input().split())
len_all = 0
word_list = []
for _ in range(N):
    temp = input()
    word_list.append(temp)
    len_all += len(temp)


bar_cnt = (M - len_all) // (N - 1)
additonal_bar_cnt = (M - len_all) % (N - 1)

for i in range(1, len(word_list)):
    temp = '_' * bar_cnt
    if 'a' <= word_list[i][0] <= 'z' and additonal_bar_cnt > 0:
        temp += '_'
        additonal_bar_cnt -= 1
    temp += word_list[i]
    word_list[i] = temp



if additonal_bar_cnt > 0:
    for i in range(len(word_list) - 1, -1, -1):
        if additonal_bar_cnt == 0:
            break
        if 'A' <= word_list[i][bar_cnt] <= 'Z' and additonal_bar_cnt > 0:
            word_list[i] = '_' + word_list[i]
            additonal_bar_cnt -= 1

ans = ''
for word in word_list:
    ans += word

print(ans)