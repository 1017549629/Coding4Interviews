

def replaceSpace(s):
    # write code here
    s_len = len(s)
    space_count = 0
    for i in s:
        if i == ' ':
            space_count += 1
    s_len += 2 * space_count
    new_array = [' '] * s_len
    j = 0
    for i in range(len(s)):  #注意这个的range很容易丢掉，忘记的话程序就不对了
        if s[i] == ' ':
            new_array[j] = '%'
            new_array[j+1] = '2'
            new_array[j+2] = '0'
            j += 3
        else:
            new_array[j] = s[i]
            j += 1
    return ''.join(new_array)
print(replaceSpace('We Are Happy'))

##更简单的方法
##不能适用于多个空格的情况，逻辑不对
def replacespace(s):
    return '%20'.join(list(s.split(' ')))
