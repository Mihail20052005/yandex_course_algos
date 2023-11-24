def check_strings(s, q, queries):
    result = []
    for query in queries:
        l, a, b = query
        substring_a = s[a:a+l]
        substring_b = s[b:b+l]
        if substring_a == substring_b:
            result.append("yes")
        else:
            result.append("no")
    return result


s = input().strip()
q = int(input().strip())
queries = []
for _ in range(q):
    query = list(map(int, input().strip().split()))
    queries.append(query)

result = check_strings(s, q, queries)
for res in result:
    print(res)