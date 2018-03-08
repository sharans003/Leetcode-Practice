import re

def replace_S(password):
    password = password.replace('s', '5')
    password = password.replace('S', '5')
    return password

def handle_odd(password):
    length = len(password)
    mid = int(length/2)
    char_mid = password[mid]
    if char_mid.isdigit():
        char_mid = str(int(char_mid) * 2)
        password = password[0:mid] + char_mid + password[mid+1:]
    return password


def handle_even(password):
    l = list(password)
    temp = l[0].swapcase()
    l[0] = l[len(password) - 1].swapcase()
    l[len(password) - 1] = temp
    password = ''.join(l)
    return password

def nextCapitalCase(password):
    string_to_check = "nextcapital"
    if any(x.isupper() for x in password) and any(x.islower() for x in password):
        index = password.lower().find(string_to_check)
        if index >= 0:
            password = password[0:index] + password[index:index+4][::-1] + password[index+4:]
    return password


def  strengthen_passwords(passwords):
    result = []
    for password in passwords:
        password = replace_S(password)
        if len(password) %2 == 1 and len(password) > 1:
            # odd
            password = handle_odd(password)
        if len(password) % 2 == 0:
            password = handle_even(password)
        password = nextCapitalCase(password)
        result.append(password)
    print(result)
    return result





if __name__ == "__main__":
    #passwords = ['nExTcapITalxnextcapital']
    passwords = ['nextCapital']
    strengthen_passwords(passwords)