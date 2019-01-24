def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def gcd2(a, b):
    while b:
        a, b = b, a%b
    return a

def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

print(gcd2(5345, 4567785))
print(gcd_recursive(5345, 34345))
