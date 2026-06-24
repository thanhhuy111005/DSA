def bai_11(adj: Dict[int, List[Tuple[int, int]]], sources: Set[int], num_vertices: int) -> List[float]:
    """Bài 11. Nhiều nguồn (Multi-source) - Sử dụng kỹ thuật thêm siêu nguồn ảo.""" [cite: 85, 86, 87]
    super_src = num_vertices
    extended_adj = {k: v.copy() for k, v in adj.items()}
    extended_adj[super_src] = []
    
    # Thêm siêu nguồn nối tới mọi nguồn thực tế với trọng số 0
    for src in sources:
        extended_adj[super_src].append((src, 0)) [cite: 87]

    dist = [float('inf')] * (num_vertices + 1)
    dist[super_src] = 0
    pq = [(0, super_src)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in extended_adj.get(u, []):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist[:num_vertices]


