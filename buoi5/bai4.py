def bai_4(dist: List[float]):
    """Bài 4. In khoảng cách tới mọi đỉnh (In -1 hoặc ∞ nếu không tới được).""" [cite: 31, 32]
    print("[Bài 4] Kết quả khoảng cách tới mọi đỉnh từ nguồn:")
    for i, d in enumerate(dist):
        display_val = d if d != float('inf') else "-1 (Không tới được)" [cite: 32]
        print(f"  -> Đỉnh {i}: {display_val}")


