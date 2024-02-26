inp = list(map(int, input().split()))
n = inp[0]
m = inp[1]
a = list(map(int, input().split()))
while m > 0:
    now = input().split()
    l, r = int(now[0])
    a = int(input().split()[1])
    a_now = a[l:r]
    print(a_now)