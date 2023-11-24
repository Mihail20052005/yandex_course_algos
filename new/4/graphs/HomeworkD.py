import heapq


def find_min_time(N, d, v, R, routes):
    graph = {i: [] for i in range(1, N + 1)}

    for r in routes:
        start, departure_time, end, arrival_time = r
        graph[start].append((end, departure_time, arrival_time))

    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[d] = 0

    heap = [(0, d)]

    while heap:
        current_time, current_node = heapq.heappop(heap)

        if current_time > dist[current_node]:
            continue

        for neighbor, departure_time, arrival_time in graph[current_node]:
            wait_time = max(0, departure_time - current_time)
            travel_time = arrival_time - current_time + wait_time

            if dist[neighbor] > current_time + travel_time:
                dist[neighbor] = current_time + travel_time
                heapq.heappush(heap, (dist[neighbor], neighbor))

    return dist[v] if dist[v] != INF else -1



N = int(input())
d, v = map(int, input().split())
R = int(input())
routes = [list(map(int, input().split())) for _ in range(R)]

result = find_min_time(N, d, v, R, routes)
print(result)
