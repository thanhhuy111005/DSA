def bai_14(adj: Dict[int, List[Tuple[int, int]]], src: int, dest: int, num_vertices: int) -> float:
    """Bài 14. Tìm độ dài đường đi ngắn nhì (Second Shortest Path, cho phép lặp cạnh).""" [cite: 95, 96]
    dist = [[float('inf'), float('inf')] for _ in range(num_vertices)] [cite: 97]
    dist[src][0] = 0
    pq = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u][1]:
            continue
        for v, w in adj.get(u, []):
            cost = d + w
            if cost < dist[v][0]:
                dist[v][1] = dist[v][0]
                dist[v][0] = cost
                heapq.heappush(pq, (cost, v))
            elif dist[v][0] < cost < dist[v][1]:
                dist[v][1] = cost
                heapq.heappush(pq, (cost, v))
    return dist[dest][1]


