stack = []
flag = True
a = input()
for i in range(len(a)):
    if a[i] == '{' or a[i] == '(' or a[i] == '[':
        stack.append(a[i])
    if len(stack) != 0:
        if a[i] == '}' and stack[len(stack) - 1] == '{':
            stack.pop(-1)
        if a[i] == ')' and stack[len(stack) - 1] == '(':
            stack.pop(-1)
        if a[i] == ']' and stack[len(stack) - 1] == '[':
            stack.pop(-1)
    elif a[i] == ')':
        flag = False
    elif a[i] == '}':
        flag = False
    elif a[i] == ']':
        flag = False

if(len(stack) == 0 and flag):
    print('yes')
else:
    print('no')