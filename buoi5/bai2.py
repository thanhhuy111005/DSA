def bai_2(adj: Dict[int, List[Tuple[int, int]]], src: int, num_vertices: int) -> List[int]:
    """Bài 2. Tính tay đường đi ngắn nhất (Ghi nhận thứ tự chốt đỉnh).""" [cite: 23, 25]
    dist = [float('inf')] * num_vertices
    visited = [False] * num_vertices
    dist[src] = 0
    order_of_settled = []

    for _ in range(num_vertices):
        u = -1
        min_d = float('inf')
        for i in range(num_vertices):
            if not visited[i] and dist[i] < min_d:
                min_d = dist[i]
                u = i
        if u == -1:
            break
        visited[u] = True
        order_of_settled.append(u)
        for v, w in adj.get(u, []):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    print(f"[Bài 2] Thứ tự các đỉnh được chốt từ nguồn {src}: {order_of_settled}") [cite: 24, 25]
    return order_of_settled


