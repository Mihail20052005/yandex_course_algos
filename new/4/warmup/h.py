first = int(input())
second = int(input())
n = int(input())
if first * second == 0:
    print('Yes' if second == 0 else 'No')
else:
    print('Yes' if first > second // n + 1 else 'No')
