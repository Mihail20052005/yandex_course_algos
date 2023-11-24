#result: ok
def is_anagr(a, b):
    return 'YES' if sorted(a) == sorted(b[::-1]) else 'NO'

a = input()
b = input()
print(is_anagr(a, b))