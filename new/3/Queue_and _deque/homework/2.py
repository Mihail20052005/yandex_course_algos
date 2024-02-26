class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        removed = self.queue.pop(0)
        return removed

    def size(self):
        return len(self.queue)

    def front(self):
        return self.queue[0]

    def clear(self):
        self.queue.clear()

    def empty(self):
        return self.queue == []

queue_1 = Queue()
queue_2 = Queue()
count = 0
str1 = input().split()
str2 = input().split()
for i in range(5):
    queue_1.push(int(str1[i]))
    queue_2.push(int(str2[i]))
while(not (queue_1.empty()) and not (queue_2.empty()) and count + 1 < 10 ** 6):
    first = queue_1.pop()
    second = queue_2.pop()

    if(first > second and  not (first == 9 and second == 0) or (first == 0 and second == 9)):
        queue_1.push(first)
        queue_1.push(second)
    if(first < second and not (second == 9 and first == 0) or (second == 0 and first == 9)):
        queue_2.push(first)
        queue_2.push(second)
    count += 1

if(queue_1.empty()):
    print('second', count)

elif(queue_2.empty()):
    print('first', count)
else:
    print('botva')


