import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    return dist

def find_path(graph, times, speeds):
    n = len(graph)
    times_to_moscow = dijkstra(graph, 0)

    max_time = 0
    last_participant = 0

    for i in range(1, n):
        time_to_moscow = times_to_moscow[i]
        time_to_prepare = times[i]
        speed = speeds[i]
        total_time = time_to_moscow / speed + time_to_prepare

        if total_time > max_time:
            max_time = total_time
            last_participant = i

    path = [last_participant + 1]
    while last_participant != 0:
        for city, _ in graph[last_participant]:
            if times_to_moscow[city] + times[city] / speeds[city] == times_to_moscow[last_participant]:
                path.append(city + 1)
                last_participant = city
                break

    path.append(1)  # Adding the capital at the end
    path.reverse()

    return max_time, path

def main():
    N = int(input())
    times = []
    speeds = []
    graph = [[] for _ in range(N)]

    for _ in range(N):
        t, v = map(int, input().split())
        times.append(t)
        speeds.append(v)

    for _ in range(N - 1):
        A, B, S = map(int, input().split())
        graph[A - 1].append((B - 1, S))
        graph[B - 1].append((A - 1, S))

    max_time, path = find_path(graph, times, speeds)

    print(f"{max_time:.10f}")
    print(" ".join(map(str, path)))

if __name__ == "__main__":
    main()
