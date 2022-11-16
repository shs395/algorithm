# 5525 - IOIOI
N = int(input())
M = int(input())
S = input()
P = 'I' + 'OI' * N
len_P = len(P)
ans = 0
idx = 0
ioi_cnt = 0
while idx < M - 2:
    if S[idx:idx+3] == 'IOI':
        ioi_cnt += 1
        if ioi_cnt == N:
            ans += 1
            ioi_cnt -= 1
        idx += 2
    else:
        idx += 1
        ioi_cnt = 0

# for i in range(M - len(P) + 1):
#     if S[i:i+len_P] == P:
#         cnt += 1
        
print(ans)