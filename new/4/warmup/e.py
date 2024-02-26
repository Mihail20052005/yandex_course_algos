def find_main(a):
    n = len(a)
    disf = 10**7
    chosen_lead = None

    for i in range(n):
        min_disf = 0

        for j in range(n):
            if i != j:
                disf += abs(a[i] - a[j])

            if disf < min_disf:
                min_disf = disf
                chosen_lead = i
    return chosen_lead

n = int(input())
a = list(map(int, input().split()))
print(find_main(a))
