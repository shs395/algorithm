# 12906 - 새로운 하노이 탑
from collections import deque

def make_visited(a, b, c):
    return '1' + a + '2' + b + '3' + c

def check_answer(a, b, c):
    if len(a) == a.count('A') and len(b) == b.count('B') and len(c) == c.count('C'):
        return True
    return False

astr = ''
bstr = ''
cstr = ''
a = input().split()
if len(a) > 1:
    astr = a[1]
b = input().split()
if len(b) > 1:
    bstr = b[1]
c = input().split()
if len(c) > 1:
    cstr = c[1]

answer = 0
queue = deque([[0, astr, bstr, cstr]])
visited = set()

while queue:
    cnt, a, b, c  = queue.popleft()
    if check_answer(a, b, c):
        answer = cnt
        break
    
    if len(a) > 0:
        atob = make_visited(a[:-1], b + a[-1], c)
        if atob not in visited:
            visited.add(atob)
            queue.append([cnt + 1, a[:-1], b + a[-1], c])
        atoc = make_visited(a[:-1], b, c + a[-1])
        if atoc not in visited:
            visited.add(atoc)
            queue.append([cnt + 1, a[:-1], b, c + a[-1]])
    
    if len(b) > 0:
        btoa = make_visited(a + b[-1], b[:-1], c)
        if btoa not in visited:
            visited.add(btoa)
            queue.append([cnt + 1, a + b[-1], b[:-1], c])
        btoc = make_visited(a, b[:-1], c + b[-1])
        if btoc not in visited:
            visited.add(btoc)
            queue.append([cnt + 1, a, b[:-1], c + b[-1]])
    
    if len(c) > 0:
        ctoa = make_visited(a + c[-1], b, c[:-1])
        if ctoa not in visited:
            visited.add(ctoa)
            queue.append([cnt + 1, a + c[-1], b, c[:-1]])
        ctob = make_visited(a, b + c[-1], c[:-1])
        if ctob not in visited:
            visited.add(ctob)
            queue.append([cnt + 1, a, b + c[-1], c[:-1]])

print(answer)