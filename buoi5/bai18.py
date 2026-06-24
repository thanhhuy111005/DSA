def bai_18():
    """Bài 18. Giải thích vì sao Dijkstra cần trọng số không âm.""" [cite: 113]
    print("[Bài 18] Nguyên nhân Dijkstra lỗi khi có trọng số âm:")
    print("  - Bản chất tham lam: Đỉnh có khoảng cách nhỏ nhất sau khi được rút khỏi hàng đợi sẽ bị 'chốt' vĩnh viễn.") [cite: 115]
    print("  - Nếu có cạnh âm (Ví dụ cạnh 2 -> 1 có trọng số -4), một đường đi vòng dài hơn về số cạnh có thể sinh ra tổng chi phí nhỏ hơn sau khi đỉnh đích đã bị chốt.") [cite: 114, 123]
    print("  - Thuật toán thay thế phù hợp: Thuật toán Bellman-Ford hoặc SPFA.") [cite: 116, 123]


