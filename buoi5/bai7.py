def bai_7(adj: Dict[int, List[Tuple[int, int]]], src: int, dest: int, num_vertices: int) -> List[int]:
    """Bài 7. Truy vết đường đi ngắn nhất (Reconstruct Path dùng mảng parent).""" [cite: 55, 56]
    dist = [float('inf')] * num_vertices
    parent = [-1] * num_vertices
    dist[src] = 0
    pq = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)
        if u == dest:
            break
        if d > dist[u]:
            continue
        for v, w in adj.get(u, []):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))

    path = []
    curr = dest
    if dist[dest] != float('inf'):
        while curr != -1:
            path.append(curr)
            curr = parent[curr]
        path.reverse()
    print(f"[Bài 7] Đường đi truy vết từ {src} đến {dest}: {' -> '.join(map(str, path))}") [cite: 56, 71]
    return path


