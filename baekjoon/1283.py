# 1283 - 단축키 지정
N = int(input())
shortcut = dict()
for _ in range(N):
    option = input().split()
    temp = ''
    flag = False
    for word in option:
        if (word[0].upper() not in shortcut and word[0].lower() not in shortcut) and flag == False:
            shortcut[word[0]] = ''
            temp += '[' + word[0] + ']' + word[1:]
            flag = True
        else:
            temp += word
        temp += ' '

    temp2 = ''
    if flag == False:
        for alphabet in temp:
            if alphabet == ' ':
                temp2 += ' '
            elif (alphabet.upper() not in shortcut and alphabet.lower() not in shortcut) and flag == False:
                shortcut[alphabet] = ''
                temp2 += '[' + alphabet + ']'
                flag = True
            else:
                temp2 += alphabet
        temp = temp2
    print(temp)