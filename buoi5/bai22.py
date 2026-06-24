def bai_22(adj: Dict[int, List[Tuple[int, int]]], src: int, dest: int, max_edges: int, num_vertices: int) -> float:
    """Bài 22. Giới hạn số cạnh trung chuyển (Trạng thái đỉnh, số_cạnh_đã_dùng).""" [cite: 138, 139, 141]
    dist_edges = [[float('inf')] * (max_edges + 1) for _ in range(num_vertices)]
    dist_edges[src][0] = 0
    pq = [(0, src, 0)]

    while pq:
        d, u, e_count = heapq.heappop(pq)
        if u == dest:
            return d
        if d > dist_edges[u][e_count]:
            continue
        if e_count < max_edges: # Phân lớp trạng thái theo số lượng cạnh [cite: 140, 141]
            for v, w in adj.get(u, []):
                if d + w < dist_edges[v][e_count + 1]:
                    dist_edges[v][e_count + 1] = d + w
                    heapq.heappush(pq, (d + w, v, e_count + 1))
                    
    ans = min(dist_edges[dest])
    return ans if ans != float('inf') else -1


