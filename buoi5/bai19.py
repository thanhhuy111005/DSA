def bai_19(adj_prob: Dict[int, List[Tuple[int, float]]], src: int, num_vertices: int) -> List[float]:
    """Bài 19. Đường đi xác suất lớn nhất (Áp dụng hàm -log quy đổi tích về tổng).""" [cite: 125, 126, 127]
    dist = [float('inf')] * num_vertices
    dist[src] = 0.0
    pq = [(0.0, src)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, p in adj_prob.get(u, []):
            w = -math.log(p) # Biến đổi phép nhân xác suất thành phép cộng trọng số âm log [cite: 127]
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
                
    return [math.exp(-d) for d in dist]


