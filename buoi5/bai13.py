def bai_13(adj: Dict[int, List[Tuple[int, int]]], src: int, num_vertices: int) -> List[int]:
    """Bài 13. Đếm số đường đi ngắn nhất từ nguồn tới mỗi đỉnh.""" [cite: 92, 93]
    dist = [float('inf')] * num_vertices
    paths_count = [0] * num_vertices
    dist[src] = 0
    paths_count[src] = 1
    pq = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj.get(u, []):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                paths_count[v] = paths_count[u]
                heapq.heappush(pq, (dist[v], v))
            elif dist[u] + w == dist[v]:
                paths_count[v] += paths_count[u]
    return paths_count


