def bai_16(adj: Dict[int, List[Tuple[int, int]]], vertex_costs: List[int], src: int, dest: int, num_vertices: int) -> float:
    """Bài 16. Trọng số trên đỉnh (Tách mỗi đỉnh v thành cặp đỉnh vào-ra u_in và u_out).""" [cite: 105, 106, 107]
    extended_adj = {}
    for u in range(num_vertices):
        u_in = u
        u_out = u + num_vertices
        extended_adj[u_in] = [(u_out, vertex_costs[u])] [cite: 106, 107]
        extended_adj[u_out] = []
        
    for u in adj:
        u_out = u + num_vertices
        for v, w in adj[u]:
            v_in = v
            extended_adj[u_out].append((v_in, w))
            
    dist = [float('inf')] * (2 * num_vertices)
    dist[src] = 0
    pq = [(0, src)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in extended_adj.get(u, []):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
                
    return dist[dest + num_vertices]


