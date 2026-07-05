def cau_15():
    print("\n--- Câu 15. Dijkstra cơ bản ---")
    # Biểu diễn đồ thị bằng danh sách kề dạng: đỉnh -> list các cặp (đỉnh_kề, trọng_số)
    graph = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}

    def dijkstra_basic(g, start):
        dist = {v: float("inf") for v in g}
        dist[start] = 0
        visited = set()

        for _ in range(len(g)):
            # Tìm đỉnh có khoảng cách nhỏ nhất chưa được viếng thăm
            u = min((v for v in g if v not in visited), key=lambda v: dist[v], default=None)
            if u is None or dist[u] == float("inf"):
                break
            visited.add(u)

            for v, weight in g[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
        return dist

    print(f"Khoảng cách ngắn nhất từ nguồn 0: {dijkstra_basic(graph, 0)}")
