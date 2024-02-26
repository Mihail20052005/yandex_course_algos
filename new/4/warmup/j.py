t = int(input())
while t > 0:
    inp = list(map(int, input().split()))
    n, a, b = inp[0], inp[1], inp[2]
    flag = False
    for i in range(a, b + 1):
        if n % i == 0:
            flag = True
    if not flag:
        if n % b in range(a, b + 1):
            flag = True
    print('YES' if flag else 'NO')
    t-=1