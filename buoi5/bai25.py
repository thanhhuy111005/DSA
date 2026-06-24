def bai_25():
    """Bài 25. Chứng minh tính đúng đắn của thuật toán Dijkstra (Bất biến tham lam).""" [cite: 151, 152]
    print("[Bài 25] Chứng minh bất biến tham lam lý thuyết:")
    print("  - Giả sử khi đỉnh u được chốt ra từ hàng đợi có khoảng cách dist[u] chưa tối ưu. Nghĩa là tồn tại một đường đi khác qua đỉnh x (chưa chốt) ngắn hơn.") [cite: 152]
    print("  - Do ràng buộc đồ thị chỉ chứa các trọng số KHÔNG ÂM, đường đi qua x đến u có tổng chiều dài: dist[x] + cost(x->u) >= dist[x].") [cite: 153]
    print("  - Nếu đường đi này ngắn hơn dist[u], dẫn đến dist[x] < dist[u]. Điều này hoàn toàn mâu thuẫn với nguyên lý hoạt động của Min-Heap (vì đỉnh x có khoảng cách nhỏ hơn đáng lẽ phải được lấy ra trước đỉnh u).") [cite: 152]
    print("  - Vì vậy, tính đúng đắn tham lam của Dijkstra được chứng minh bằng phản chứng thành công.") [cite: 152]


