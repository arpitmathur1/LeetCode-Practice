def is_palindrome( s, left,right):
    print(s[left:right])
    return True if s[left:right] == s[left:right][::-1] else False


print(is_palindrome("asdfdsa", 3,4))