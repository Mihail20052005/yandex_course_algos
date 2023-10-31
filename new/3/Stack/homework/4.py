stack = []
answ = 0
n = int(input())
a = list(map(int, input().split()))

for i in a:

    stack.append(i)
    if len(stack) != 0:
        while(len(stack) != 0 and stack[-1] == (answ + 1)):
            answ = stack[-1]
            stack.pop()
if len(stack) == 0 and answ == max(a):
    print('YES')
else:
    print('NO')
