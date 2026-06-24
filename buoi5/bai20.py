def bai_20(adj: Dict[int, List[Tuple[int, int]]], src: int, dest: int, num_vertices: int, K: int) -> List[int]:
    """Bài 20. Tìm K đường đi ngắn nhất (Cho phép một đỉnh được lấy ra tối đa K lần).""" [cite: 129, 130, 131]
    count_extracted = [0] * num_vertices
    result_paths = []
    pq = [(0, src)]

    while pq and count_extracted[dest] < K:
        d, u = heapq.heappop(pq)
        count_extracted[u] += 1 [cite: 131]
        
        if u == dest:
            result_paths.append(d)
            
        if count_extracted[u] <= K:
            for v, w in adj.get(u, []):
                heapq.heappush(pq, (d + w, v))
                
    return result_paths


