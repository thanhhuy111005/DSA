def cau_19():
    print("\n--- Câu 19. Đường đi ngắn nhất trên lưới ---")
    import heapq

    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]  # Lưới chi phí di chuyển

    def shortest_path_grid(matrix):
        R, C = len(matrix), len(matrix[0])
        dist = [[float("inf")] * C for _ in range(R)]
        dist[0][0] = matrix[0][0]
        min_heap = [(matrix[0][0], 0, 0)]  # (cost, r, c)

        while min_heap:
            d, r, c = heapq.heappop(min_heap)
            if r == R - 1 and c == C - 1:
                return d
            if d > dist[r][c]:
                continue

            # Đi 4 hướng kề cận
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    if dist[r][c] + matrix[nr][nc] < dist[nr][nc]:
                        dist[nr][nc] = dist[r][c] + matrix[nr][nc]
                        heapq.heappush(min_heap, (dist[nr][nc], nr, nc))
        return -1

    print(f"Tổng chi phí nhỏ nhất từ đỉnh trái-trên xuống phải-dưới: {shortest_path_grid(grid)}")
