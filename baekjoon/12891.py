# 12891 - DNA 비밀번호
S, P = map(int, input().split())
DNA = input()
A, C, G, T = map(int, input().split())
cnt = { 'a':0, 'c':0, 'g':0, 't':0 }
ans = 0
DNA = DNA.lower()
temp = DNA[:P]
cnt['a'] = temp.count('a')
cnt['c'] = temp.count('c')
cnt['g'] = temp.count('g')
cnt['t'] = temp.count('t')
if cnt['a'] >= A and cnt['c'] >= C and cnt['g'] >= G and cnt['t'] >= T:
    ans += 1
for i in range(1, S - P + 1):
    cnt[DNA[i - 1]] -= 1
    cnt[DNA[i + P - 1]] += 1
    if cnt['a'] >= A and cnt['c'] >= C and cnt['g'] >= G and cnt['t'] >= T:
        ans += 1
    
print(ans)