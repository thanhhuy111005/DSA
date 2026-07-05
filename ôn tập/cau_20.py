def cau_20():
    print("\n--- Câu 20. Dijkstra vs Bellman-Ford vs A* ---")
    print("So sánh tổng quan cấu trúc đồ thị:")
    print("- Dijkstra: Chỉ áp dụng cho đồ thị trọng số không âm. Độ phức tạp: O((V+E)log V) khi dùng heap.")
    print("- Bellman-Ford: Chấp nhận đồ thị có cạnh âm, phát hiện được chu trình âm. Độ phức tạp chậm hơn: O(V*E).")
    print("- A*: Thêm hàm Heuristic h(n) dự đoán khoảng cách tới đích, giúp định hướng thu hẹp không gian duyệt.")
    print("      Duyệt ít đỉnh hơn đáng kể nếu có một hàm heuristic tốt và chính xác.")


# ==============================================================================
# 4. NGĂN XẾP (STACK - LIFO)
# ==============================================================================
