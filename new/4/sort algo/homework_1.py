n = int(input())
a = list(map(int, input().split()))
x = int(input())

def partition(x, array):
    less, big = 0,0
    for i in range(n):
        if array[i] < x:
            less += 1
            array[i], array[less] = array[less], array[i]
        else:
            big += 1
    return (less, big)

result = partition(x, a)
print(result[0])
print(result[1])
