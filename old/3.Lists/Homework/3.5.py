x, y, z = [int(i) for i in input().split()]
n = list(input())

n = set(n)
len_n = len(n)
if str(x) in n:
    len_n -= 1
if str(y) in n:
    len_n -= 1
if str(z) in n:
    len_n -= 1
print(len_n)
