# 1512 - 주기문으로 바꾸기
M = int(input())
string = input()
len_string = len(string)
ans = 3001
data = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
for i in range(1, M + 1):
    temp = [[0 for _ in range(4)] for _ in range(i)]
    cnt = 0
    for j in range(len(string)):
        temp[j % i][data[string[j]]] += 1
    for j in range(len(temp)):
        cnt += sum(temp[j]) - max(temp[j])
    ans = min(cnt, ans)
print(ans)