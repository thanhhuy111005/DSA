def bai_24():
    """Bài 24. So sánh lý thuyết giữa Dijkstra vs Bellman-Ford vs A*.""" [cite: 146, 147]
    print("[Bài 24] So sánh tổng quan các thuật toán:")
    print("  - Dijkstra: Ràng buộc đồ thị không có cạnh âm, độ phức tạp đạt O((V+E)log V). Không dùng hàm bổ trợ.") [cite: 147]
    print("  - Bellman-Ford: Cho phép đồ thị chứa cạnh âm, kiểm tra được chu trình âm, chi phí lớn O(V*E).") [cite: 147]
    print("  - A*: Tích hợp thêm hàm ước lượng Heuristic tốt giúp định hướng không gian duyệt tìm kiếm tới đích cực nhanh.") [cite: 147, 148, 149]


