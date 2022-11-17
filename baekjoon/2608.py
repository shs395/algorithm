# 2608 - 로마 숫자
a = input()
b = input()
data = {
    'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 
    'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900
}

data2 = dict()

for d in data:
    data2[data[d]] = d

def change(string):
    i = 0
    cnt = 0
    while i < len(string):
        if i + 1 < len(string) and data[string[i]] < data[string[i + 1]]:
            cnt += data[string[i:i+2]]
            i += 2
        else:
            cnt += data[string[i]]
            i += 1
    return cnt

def change2(num):
    temp = list(data2.keys())
    temp.sort(reverse=True)
    string = ''
    while num > 0:
        for t in temp:
            if num >= t:
                num -= t
                string += data2[t]
                break
    return string


ans = change(a) + change(b)
print(ans)
print(change2(ans))