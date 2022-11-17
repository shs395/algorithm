# 12904 - A와 B
S = input()
T = input()


# while len(T) > len(S):
#     if T[-1] == 'A':
#         T = T[:-1]
#     else:
#         T = T[:-1][::-1]


# 뒤에서 살 필 경우 True , 앞에서 볼 경우 False
flag = True
while len(T) > len(S):
    if flag == True:
        if T[-1] == 'B':
            flag = False
        T = T[:-1]
        
    else:
        if T[0] == 'B':
            flag = True
        T = T[1:]

if flag == False:
    T = T[::-1]
    
if T == S:
    print(1)
else:
    print(0)