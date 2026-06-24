def bai_21(adj: Dict[int, List[Tuple[int, int]]], src: int, dest: int, max_fuel: int, fuel_costs: List[int], num_vertices: int) -> int:
    """Bài 21. Dijkstra trên trạng thái mở rộng State = (đỉnh, nhiên liệu).""" [cite: 133, 134, 136]
    # dist_state[u][fuel] lưu chi phí nạp nhiên liệu rẻ nhất [cite: 135]
    dist_state = [[float('inf')] * (max_fuel + 1) for _ in range(num_vertices)]
    dist_state[src][0] = 0
    pq = [(0, src, 0)] 

    while pq:
        cost, u, fuel = heapq.heappop(pq)
        if u == dest:
            return cost
        if cost > dist_state[u][fuel]:
            continue
        
        # Thao tác nạp thêm nhiên liệu tại đỉnh hiện tại u [cite: 137]
        if fuel < max_fuel:
            if cost + fuel_costs[u] < dist_state[u][fuel + 1]:
                dist_state[u][fuel + 1] = cost + fuel_costs[u]
                heapq.heappush(pq, (dist_state[u][fuel + 1], u, fuel + 1))
                
        # Thao tác di chuyển sang đỉnh kề v tiêu tốn w đơn vị nhiên liệu
        for v, w in adj.get(u, []):
            if fuel >= w:
                if cost < dist_state[v][fuel - w]:
                    dist_state[v][fuel - w] = cost
                    heapq.heappush(pq, (cost, v, fuel - w))
    return -1


