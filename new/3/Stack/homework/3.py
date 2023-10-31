from collections import deque
stack = []
a = input().split()
for i in a:
    if(i == '+' or i == '-' or i == '*'):
        result = 0
        if i == '+':
            result = int(stack[len(stack) - 2]) + int(stack[len(stack) - 1])
            stack.pop(-1)
            stack.pop(-1)
            stack.append(result)
        elif i == '-':
            result = int(stack[len(stack) - 2]) - int(stack[len(stack) - 1])
            stack.pop(-1)
            stack.pop(-1)
            stack.append(result)

        elif i == '*':
            result = int(stack[len(stack) - 2]) * int(stack[len(stack) - 1])
            stack.pop(-1)
            stack.pop(-1)
            stack.append(result)
    else:
        stack.append(int(i))
print(stack[0])

