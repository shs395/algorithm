# 17609 - 회문
import sys
input = sys.stdin.readline
T = int(input().rstrip())

def a(temp):
    i = 0
    j = len(temp) - 1
    while i < j:
        count = 0
        if temp[i] == temp[j]:
            i += 1
            j -= 1
        else:
            if temp[i + 1:j + 1] == temp[i + 1:j + 1][::-1]:
                return True
            elif temp[i:j] == temp[i:j][::-1]:
                return True
            else:
                return False
    return True

for _ in range(T):
    temp = input().rstrip()
    if temp == temp[::-1]:
        print(0)
    elif a(temp) == True:
        print(1)
    else:
        print(2)
