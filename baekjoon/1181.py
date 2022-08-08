# 1181 - 단어 정렬
def setting(x):
    return len(x)
    
N = int(input())
words = []
answer = []
for i in range(N):
    words.append(input())
words.sort()
words.sort(key=setting)

for i in words:
    if i not in answer:
        answer.append(i)

for i in answer:
    print(i)
