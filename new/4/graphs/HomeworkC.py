import heapq

def dijkstra(graph, start, end):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start - 1] = 0
    heap = [(0, start)]

    while heap:
        d, node = heapq.heappop(heap)

        if dist[node - 1] < d:
            continue

        for neighbor, weight in graph[node - 1]:
            if dist[node - 1] + weight < dist[neighbor - 1]:
                dist[neighbor - 1] = dist[node - 1] + weight
                heapq.heappush(heap, (dist[neighbor - 1], neighbor))

    return dist[end - 1] if dist[end - 1] != float('inf') else -1

N, K = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(K):
    a, b, l = map(int, input().split())
    graph[a - 1].append((b, l))
    graph[b - 1].append((a, l))

A, B = map(int, input().split())

result = dijkstra(graph, A, B)

print(result)
