def bai_6(adj: Dict[int, List[Tuple[int, int]]], src: int, dest: int, num_vertices: int) -> float:
    """Bài 6. Đường đi ngắn nhất giữa hai đỉnh (Tối ưu dừng sớm).""" [cite: 52, 53]
    dist = [float('inf')] * num_vertices
    dist[src] = 0
    pq = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)
        if u == dest: # Dừng sớm ngay khi lấy được đích ra khỏi hàng đợi [cite: 53]
            break
        if d > dist[u]:
            continue
        for v, w in adj.get(u, []):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist[dest]


