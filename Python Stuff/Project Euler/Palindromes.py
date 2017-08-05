
def reverse(s):
    rev = ''
    for c in s:
        rev = c + rev
    return rev

def reverse_v2(s):
    n = len(s)
    return s[:n//2] == reverse(s[n-n//2:])

def reverse_v3(s):
    i = 0
    j = len(s) - 1
    
    while i<j and s[i] == s[j]:
        i = i + 1
        j = j - 1
    return j <= i
