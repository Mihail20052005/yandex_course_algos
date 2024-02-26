a = set(int(i) for i in input().split())
b = set(int(i) for i in input().split())
for i in a:
    if i in b:
        print(i, end=' ')