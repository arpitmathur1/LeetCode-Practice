i = 3

binary_string = bin(i)
if len([ch for ch in binary_string if ch == '1']) == 1:
    print("power of two")
else:
    print("not power of two")