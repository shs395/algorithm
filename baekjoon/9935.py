# 9935 - 문자열 폭발
string = input()
bomb = input()
bomb_len = len(bomb)
last_bom = bomb[-1]
stack = []

for s in string:
    stack.append(s)
    if s == last_bom and ''.join(stack[-bomb_len:]) == bomb:
        for _ in range(bomb_len):
            stack.pop()
        # stack = stack[:-bomb_len]

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))

# 슬라이싱시 시간 초과, pop 사용시 통과
# pop은 O(1) 코드상 폭발문자열의 최대는 36이므로 36번 연산
# 슬라이싱은 a[i:k] 의 경우 O(k - i) , 스택의 길이가 길어질 수록 원래 코드는 극히 비효율적
# 현재 문자가 폭탄의 마지막 문자와 같을 경우를 조건으로 추가해서 시간 단축 가능