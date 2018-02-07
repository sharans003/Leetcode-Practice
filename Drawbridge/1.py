'''
first question is the parentheses match, function signature is int [] balanceOrnot (String [] strs, int [] maxReplacement),
strs [i] corresponds to a string such as "<< >>>>", and the function determines whether strs can be replaced by a
maxReplaement to become a form of parentheses matching. Note that the replacement rule is> can be replaced by <>, so that
matches. But <can not be replaced by <>. Function returns an array, the array represents strs can be successfully replaced
'''



'''
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
        
'''
def balanceornot(strs, maxreplacement):
    valid_list = []
    for i in range(0, len(strs)):
        input = strs[i]
        max_mistakes = maxreplacement[i]

        parenthesis_dict = {}
        parenthesis_dict['>'] = '<'
        allowed_mistakes = ['>']

        stack = []
        mistakes_tracker = 0
        exceeded = False
        for char in input:
            if char in parenthesis_dict.values():
                stack.append(char)
            elif char in parenthesis_dict.keys():
                if stack  == [] or parenthesis_dict[char] != stack.pop():
                    if char in allowed_mistakes:
                        mistakes_tracker += 1
                        if mistakes_tracker > max_mistakes:
                            exceeded = True
                            break
                    else:
                        exceeded = True
                        break

        if not exceeded and stack == []:
            valid_list.append(input)
    return valid_list


if __name__ == "__main__":
    strs = ['<<>>', '<>>', '<<>','<><>','<>>']
    maxreplacement = [1,1,5,0,0]
    print(balanceornot(strs, maxreplacement))



