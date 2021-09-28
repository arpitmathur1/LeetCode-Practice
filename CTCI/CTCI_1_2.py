from collections import defaultdict

string = "abacaab"
def palindrome_permutation(string):
    data = defaultdict(int)
    counts = defaultdict(int)
    counts[0] = len(string)
    
    for ch in string:
        data[ch] += 1
        counts[data[ch]] += 1
        counts[data[ch]-1] += 1
    
    odds = 0
    print(counts)
    for c in counts.keys():
        print(c)
        if c % 2 == 1:
            
            odds += 1
    print(data)
    return True if odds < 2 else False

print(palindrome_permutation(string))