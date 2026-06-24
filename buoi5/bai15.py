def bai_15(grid: List[List[int]]) -> int:
    """Bài 15. Dijkstra trên lưới chi phí (Grid 3x3, di chuyển 4 hướng).""" [cite: 99, 100, 101]
    R, C = len(grid), len(grid[0])
    dist = [[float('inf')] * C for _ in range(R)]
    dist[0][0] = grid[0][0]
    pq = [(grid[0][0], 0, 0)]

    while pq:
        d, r, c = heapq.heappop(pq)
        if r == R - 1 and c == C - 1:
            return d
        if d > dist[r][c]:
            continue
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]: [cite: 101]
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                if d + grid[nr][nc] < dist[nr][nc]:
                    dist[nr][nc] = d + grid[nr][nc]
                    heapq.heappush(pq, (dist[nr][nc], nr, nc))
    return -1


