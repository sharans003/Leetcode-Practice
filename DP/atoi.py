def myAtoi(s):
    if len(s) == 0:
        return 0

    s = s.strip()
    index = 0
    flag = 1
    if s[0] == '+':
        flag = 1
        index += 1
    elif s[0] == '-':
        flag = -1
        index +=1

    result = 0
    max_int = 2**31 -1
    min_int = -2**31
    while(index < len(s)):
        if s[index] >= '0' and s[index] <= '9':
            print('valid')
            result = result*10 + ord(s[index]) - ord('0')
            index+= 1
        else:
            break;


    if flag*result > max_int:
        return max_int
    elif flag*result < min_int:
        return min_int
    return flag*result




# Driver program
string = "-123"

print(myAtoi(string))

