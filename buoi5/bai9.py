def bai_9(adj: Dict[int, List[Tuple[int, int]]], src: int, num_vertices: int) -> List[float]:
    """Bài 9. Dijkstra với hàng đợi ưu tiên (Min-Heap / Priority Queue O((V+E)log V)).""" [cite: 77, 78]
    dist = [float('inf')] * num_vertices
    dist[src] = 0
    pq = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj.get(u, []):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist


