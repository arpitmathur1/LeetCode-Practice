'''
from collections import Counter

string = "asdfargfjrue"

c = Counter(string)
print(c)
print( set(c.values()) == {1} )
print(c.keys())


from collections import defaultdict

d = defaultdict(lambda : [])
d = defaultdict(list)
d[0].append("hi")

print(d)
'''

## CTCI problem #1
string = "asdfglkhpiuwmnb"


def unique_char_string(string):
    for left_idx in range(len(string)):
        for right_idx in range( left_idx+1, len(string) ):
            if string[left_idx] == string[right_idx]:
                return False
    return True

print(unique_char_string(string))


from collections import defaultdict
def unique_char_string_1(string):
    hash_ = defaultdict(int)
    
    for char in string:
        if char in hash_.keys():
            return False
        hash_[char] += 1
    return True

print(unique_char_string_1(string))















