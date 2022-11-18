# 6137 - 문자열 생성
import sys
input = sys.stdin.readline
N = int(input().rstrip())
string = ''
T = ''
for _ in range(N):
    string += input().rstrip()

left_idx = 0
right_idx = len(string) - 1
while len(T) < len(string):
    if string[left_idx] < string[right_idx]:
        T += string[left_idx]
        left_idx += 1
        
    elif string[left_idx] > string[right_idx]:
        T += string[right_idx]
        right_idx -= 1

    else:
        flag = False
        temp_left_idx = left_idx + 1
        temp_right_idx = right_idx - 1
        while temp_left_idx < temp_right_idx:
            if string[temp_left_idx] < string[temp_right_idx]:
                T += string[left_idx]
                left_idx += 1
                flag = True
                break
            elif string[temp_left_idx] > string[temp_right_idx]:
                T += string[right_idx]
                right_idx -= 1
                flag = True
                break
            else:
                temp_left_idx += 1
                temp_right_idx -= 1
        
        if flag == False:
            T += string[left_idx]
            left_idx += 1
               

for i in range(len(T)):
    print(T[i], end='')
    if (i + 1) % 80 == 0:
        print()
