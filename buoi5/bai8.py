def bai_8(dist: List[float], D: float) -> int:
    """Bài 8. Đếm số đỉnh trong bán kính D (Khoảng cách từ nguồn <= D).""" [cite: 73, 74]
    count = sum(1 for d in dist if d <= D) [cite: 74]
    print(f"[Bài 8] Số đỉnh nằm trong bán kính D = {D}: {count}") [cite: 74]
    return count


