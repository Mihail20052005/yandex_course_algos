stack = []
while(True):
    command = input()
    if command == 'size':
        print(len(stack))
    if command[0:4] == 'push':
        result = command[4::]
        stack.append(int(result))
        print('ok')
    if command == 'back':
        if len(stack) != 0:
            print(stack[len(stack) - 1])
        else:
            print('error')
    if command == 'pop':
        if len(stack) != 0:
            print(stack[len(stack) - 1])
            stack.pop(-1)

        else:
            print('error')
    if command == 'clear':
        stack.clear()
        print('ok')
    if command == 'exit':
        print('bye')
        break