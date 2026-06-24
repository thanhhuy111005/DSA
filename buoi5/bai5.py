def bai_5():
    """Bài 5. Đồ thị vô hướng có trọng số G2 (Thành phố A tới các thành phố còn lại).""" [cite: 35, 36, 37]
    num_vertices = 5
    dist = [float('inf')] * num_vertices
    dist[0] = 0 # Đỉnh 0 đại diện cho thành phố A [cite: 51]
    pq = [(0, 0)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph_G2[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    mapping = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'} [cite: 51]
    result = {mapping[i]: int(dist[i]) for i in range(num_vertices) if dist[i] != float('inf')}
    print(f"[Bài 5] Khoảng cách ngắn nhất trên G2 từ A: {result}") [cite: 51]


