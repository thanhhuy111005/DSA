def cau_16():
    print("\n--- Câu 16. Truy vết đường đi ---")
    graph = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}

    def dijkstra_trace(g, start, target):
        dist = {v: float("inf") for v in g}
        parent = {v: None for v in g}  # Mảng parent phục vụ truy vết ngược
        dist[start] = 0
        visited = set()

        for _ in range(len(g)):
            u = min((v for v in g if v not in visited), key=lambda v: dist[v], default=None)
            if u is None or dist[u] == float("inf"):
                break
            visited.add(u)

            for v, weight in g[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    parent[v] = u  # Ghi nhớ đỉnh cha

        # Truy ngược đường đi từ target về start
        path = []
        curr = target
        while curr is not None:
            path.append(curr)
            curr = parent[curr]
        path.reverse()
        return path

    print(f"Đường đi từ 0 tới 3: {' -> '.join(map(str, dijkstra_trace(graph, 0, 3)))}")
