n = int(input())
usedBefore = set()
for i in range(n):
    a,b = map(int, input().split())
    if a >= 0 and b >= 0 and a + b == n - 1 and a not in usedBefore:
        usedBefore.add(a)
print(len(usedBefore))