n = int(input())
a = list(map(int, input().split()))
k = int(input())
b = list(map(int, input().split()))

def merge(n, a, k, b):
    min_len = min(len(a), len(b))
    answer = []
    flag_a = 0
    flag_b = 0

    if len(a) == 0 or len(b) == 0:
        print(0)
    else:
        while(True):
            if a[flag_a] < b[flag_b]:
                answer.append(a[flag_a])
                flag_a += 1
            else:
                answer.append(b[flag_b])
                flag_b += 1
            if flag_a == len(a):
                while (flag_b != len(b)):
                    answer.append(b[flag_b])
                    flag_b += 1
                break
            elif flag_b == len(b):
                while(flag_a != len(a)):
                    answer.append(a[flag_a])
                    flag_a += 1
                break
        return answer
