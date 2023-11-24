def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


a, b, c, d = map(int, input().split())
num = a * d + b * c
denom = c * d
t = gcd(num, denom)
print(num // t, denom // t)