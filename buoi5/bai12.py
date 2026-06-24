def bai_12(adj: Dict[int, List[Tuple[int, int]]], s: int, t: int, k: int, num_vertices: int) -> float:
    """Bài 12. Đi qua đỉnh bắt buộc k (Tính đường đi ngắn nhất s -> k -> t).""" [cite: 89, 90]
    dist_from_s = bai_9(adj, s, num_vertices)
    dist_from_k = bai_9(adj, k, num_vertices)
    total_dist = dist_from_s[k] + dist_from_k[t] [cite: 90]
    print(f"[Bài 12] Khoảng cách từ {s} đến {t} bắt buộc qua {k}: {total_dist}") [cite: 91]
    return total_dist


