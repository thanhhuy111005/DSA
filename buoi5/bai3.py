def bai_3(adj: Dict[int, List[Tuple[int, int]]], src: int, num_vertices: int) -> List[float]:
    """Bài 3. Dijkstra cơ bản: nguồn tới mọi đỉnh (Bản O(V^2)).""" [cite: 27, 28]
    dist = [float('inf')] * num_vertices
    visited = [False] * num_vertices
    dist[src] = 0

    for _ in range(num_vertices):
        u = -1
        min_d = float('inf')
        for i in range(num_vertices):
            if not visited[i] and dist[i] < min_d:
                min_d = dist[i]
                u = i
        if u == -1 or dist[u] == float('inf'):
            break
        visited[u] = True
        for v, w in adj.get(u, []):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist


