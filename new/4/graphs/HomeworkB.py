import heapq

def dijkstra(graph, start, end):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start - 1] = 0
    prev = [-1] * n
    heap = [(0, start)]

    while heap:
        d, node = heapq.heappop(heap)

        if dist[node - 1] < d:
            continue

        for neighbor, weight in enumerate(graph[node - 1]):
            if weight >= 0:
                if dist[node - 1] + weight < dist[neighbor]:
                    dist[neighbor] = dist[node - 1] + weight
                    prev[neighbor] = node

                    heapq.heappush(heap, (dist[neighbor], neighbor + 1))

    path = []
    current = end
    while current != -1:
        path.insert(0, current)
        current = prev[current - 1]

    return path

N, S, F = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

shortest_path = dijkstra(graph, S, F)

if shortest_path[0] == -1:
    print(-1)
else:
    print(" ".join(map(str, shortest_path)))
