import re

def isNumber(s):
    regex_string = "[+-]{0,1}[0-9]*[.]{0,1}[0-9]{1,}[eE]{0,1}[0-9]*"
    try:
        find = re.findall(regex_string, s)
    except Exception:
        return False
    print(find)
    if len(find) > 0:
        return find[0] == s
    else:
        return False

isNumber('0')