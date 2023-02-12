def time_to_minute(s):
    h, m = s.split(':')
    return 60 * int(h) + int(m)

def convert(s):
    temp = ''
    for c in s:
        if c == '#':
            a = temp[-1].lower()
            temp = temp[:-1]
            temp += a
        else:
            temp += c
    return temp
            
def solution(m, musicinfos):
    answer = ''
    data = []
    
    for musicinfo in musicinfos:
        temp_music = ''
        start, end, name, music = musicinfo.split(',')
        time = time_to_minute(end) - time_to_minute(start)
        convert_music = convert(music)
        temp_music += convert_music * (time // len(convert_music))
        temp_music += convert_music[:time % len(convert_music)]
        data.append([time, temp_music, name])
        
    data.sort(key=lambda x:x[0], reverse=True)
    convert_m = convert(m)
    
    for x in data:
        if convert_m in x[1]:
            return x[2]
           
    return '(None)'
