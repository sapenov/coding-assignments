"""
fnr is 4x faster than fnr2
a) creation of the new string is about O(N) operations,
b) the string length is reduced (in some cases significantly) at every step
c) in most cases algorithm stops before processing the rest of the string.
"""

def fnr(s):
    while s != "":
        slen0 = len(s)
        ch = s[0]
        s = s.replace(ch, "")
        slen1 = len(s)
        if slen1 == slen0 - 1:
            print(ch)
            break
    else:
        print("No answer")

print(fnr("aabccbdcbe"))

def fnr2(s):
    rty = [a for a in s if s.count(a) == 1][0]
    return rty

print(fnr2("aabccbdcbe"))

print(fnr2([123,1231,544,66,43,123,22,6,8,9,4,86]))

print(fnr2(['g','v','v','g','j','k']))
