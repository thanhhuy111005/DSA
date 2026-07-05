def cau_28():
    print("\n--- Câu 28. BFS dùng hàng đợi ---")
    graph = {0: [1, 2], 1: [3], 2: [3], 3: []}

    def bfs_traverse(g, start):
        visited = set([start])
        queue = deque([start])  # Sử dụng hàng đợi chuẩn để lấy phần tử theo tầng
        order = []

        while queue:
            u = queue.popleft()
            order.append(u)
            for v in g[u]:
                if v not in visited:
                    visited.add(v)
                    queue.append(v)
        return order

    print(f"Thứ tự duyệt BFS từ đỉnh gốc 0: {bfs_traverse(graph, 0)}")
