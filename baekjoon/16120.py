# 16120 - PPAP
string = input()
stack = []
def check(stack):
    while len(stack) >= 4:
        if ''.join(stack[-4:]) == 'PPAP':
            stack.pop()
            stack.pop()
            stack.pop()
        else:
            break
    return 

for c in string:
    stack.append(c)
    if len(stack) >= 4:
        check(stack)

if len(stack) == 1 and stack[0] == 'P':
    print('PPAP')
else:
    print('NP')