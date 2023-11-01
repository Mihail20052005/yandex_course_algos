class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if len(self.queue) == 0:
            print('error')
            return None
        removed = self.queue.pop(0)
        print(removed)
        return removed

    def size(self):
        print(len(self.queue))
        return len(self.queue)

    def front(self):
        if len(self.queue) != 0:
            print(self.queue[0])
            return self.queue[0]
        else:
            print('error')
            return None

    def clear(self):
        self.queue.clear()
        print('ok')


q = Queue()
s = input()
if s[0] == 'exit':
    print('bye')
else:
    while s != 'exit':
        s = s.split()
        if s[0] == 'push':
            q.push(int(s[1]))
            print('ok')
        elif s[0] == 'front':
            q.front()
        elif s[0] == 'pop':
            q.pop()
        elif s[0] == 'size':
            q.size()
        elif s[0] == 'clear':
            q.clear()
        s = input()
    print('bye')
