def longestPalindrome(s):
    start = end = 0

    for i in range(len(s)):
        len1 = expandAroundCenter(s, i, i)
        len2 = expandAroundCenter(s, i, i+1);
        length = max(len1, len2)
        if length > end - start:
            start  = int(i - int((length -1)/2))
            end = int(i + length/2)
    print('start and end are: ',start,", ",end)
    print(type(start))
    print(type(end))
    print(s)
    return s[int(start),int(end+1)]

def expandAroundCenter(s,left,right):
    L = left
    R = right

    while L >=0 and R < len(s) and s[L] == s[R]:
        L-= 1
        R+= 1
    return R - L - 1

if __name__ == "__main__":
    s = 'aba'
    print(longestPalindrome(s))