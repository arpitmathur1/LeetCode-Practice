'''
Some test cases:
    
[]
    []

["a"]
    ["a"]

["a", "a"]    ======
    ["a", "2"]

["a", "b"]
    ["a", "b"]

["a", "a", "a", "b"]   ======
    ["a", "2", "b"]

["a", "a", "a", "b", "a", "a", "a", "b", "b"]
    ["a", "3", "b", "a", "3", "b", "2"]

["a", "a", "a", "b", "a", "a", "a", "b", "b", "a"] ========
    ["a", "3", "b", "a", "3", "b", "2", "a"]

["a", "a", "a", "b", "a", "a", "a", "b", "c", "a"]
    ["a", "3", "b", "a", "3", "b", "c", "a"]

["a", "a", "b", "a", "c", "a", "c", "d", "e"]
    ["a", "2", "b", "a", "c", "a", "c", "d", "e"]
'''

'''
current_string, current_string_start = "", -1
loop through idx:
    if same string found, continue
    
    if new string found, 
        if idx == current_string_start+1:
            current_string = list[idx]
        remove strings from current_string_start+1 to current location with str(integer)
'''


def compress_string(chars):
    
    if len(chars) == 0:
        return []
    
    print()
    current_string, current_string_start = chars[0], 0
    final = []
    
    final.append(chars[current_string_start])
    for idx in range(1, len(chars)):
        #print(idx, chars[idx], final)
        if current_string == chars[idx]:
            if idx == len(chars)-1:
                final.append( str(idx-current_string_start+1) )
        else:
            if idx != current_string_start+1:
                final.append( str(idx-current_string_start) )
            
            current_string = chars[idx]
            current_string_start = idx
            final.append(chars[current_string_start])
    return final
    
    
print(compress_string([]))
#    []

print(compress_string(["a"]))
#    ["a"]

print(compress_string(["a", "a"]))
#    ["a", "2"]

print(compress_string(["a", "b"]))
#    ["a", "b"]

print(compress_string(["a", "a", "a", "b"]))
#    ["a", "3", "b"]

print(compress_string(["a", "a", "a", "b", "a", "a", "a", "b", "b"]))
#    ["a", "3", "b", "a", "3", "b", "2"]

print(compress_string(["a", "a", "a", "b", "a", "a", "a", "b", "b", "a"]))
#    ["a", "3", "b", "a", "3", "b", "2", "a"]

print(compress_string(["a", "a", "a", "b", "a", "a", "a", "b", "c", "a"]))
#    ["a", "3", "b", "a", "3", "b", "c", "a"]

print(compress_string(["a", "a", "b", "a", "c", "a", "c", "d", "e"]))
#    ["a", "2", "b", "a", "c", "a", "c", "d", "e"]


























