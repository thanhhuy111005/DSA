def bai_17(adj: Dict[int, List[Tuple[int, int]]], src: int, num_vertices: int) -> List[float]:
    """Bài 17. Đường đi bottleneck (Minimax: Cạnh lớn nhất trên đường là nhỏ nhất).""" [cite: 109, 110]
    dist = [float('inf')] * num_vertices
    dist[src] = 0
    pq = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj.get(u, []):
            # Sửa đổi biểu thức cập nhật (Relax) của bài toán cổ chai minimax
            max_edge_on_path = max(dist[u], w) [cite: 111, 112]
            if max_edge_on_path < dist[v]:
                dist[v] = max_edge_on_path
                heapq.heappush(pq, (dist[v], v))
    return dist


