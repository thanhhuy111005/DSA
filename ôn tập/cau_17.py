def cau_17():
    print("\n--- Câu 17. Dijkstra với heap ---")
    import heapq

    graph = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}

    def dijkstra_heap(g, start):
        dist = {v: float("inf") for v in g}
        dist[start] = 0
        min_heap = [(0, start)]  # Hàng đợi ưu tiên lưu cặp (khoảng_cách, đỉnh)

        while min_heap:
            d, u = heapq.heappop(min_heap)
            if d > dist[u]:
                continue

            for v, weight in g[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(min_heap, (dist[v], v))
        return dist

    print(f"Dijkstra dùng Heap đạt hiệu năng O((V+E)log V): {dijkstra_heap(graph, 0)}")
