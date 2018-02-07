'''The second question is the use of aeiou five characters to meet the length and requirements of the string number,
function signature is int magicString (int n). There are certain conditions,
such as a behind only e, e behind only a / i, i behind only a / e / o / u, o behind only i / u, u only I
s a I did not figure out whether there is any law of this requirement. . Recursive to write the normal violence,
the last six cases out of time. . Feel should be stored memory, such as a behind the number of e to save down,
and then i behind the number of e can be obtained directly. . . It was really no time to write at that time. . .


https://www.reddit.com/r/Programing_Challenges/comments/6gwyb8/find_longest_subsequence_of_string/
'''



def magical(s,chars):
    if(len(s) == 0 or len(chars) == 0):
        return 0

    if (len(s) < len(chars)):
        return 0

    if  len(s) == len(chars) :
        for i in range(0, len(s)):
            if s[i] != chars[i]:
                return 0
        return len(s)

    if s[0] < chars[0]:
        return magical(s[1:], chars)
    elif s[0] == chars[0]:
        removing_first_s = s[1:]
        removing_first_char = chars[1:]
        return max(

                    max( (1 + magical(removing_first_s, removing_first_char)),
                          (1 + magical(removing_first_s, chars))
                        ),

                    magical(removing_first_s, chars)
                )
    else:
        removing_first_s = s[1:]
        return magical(removing_first_s, chars)










if __name__ =="__main__":
    chars = ['a', 'e', 'i', 'o', 'u']
    inps = ["aeiaaioooaauuaeiou", "aaejkioou", "uopqraeizzzou"]

    for inp in inps:
        m = magical(inp, chars)
        print(m)
