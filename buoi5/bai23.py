def bai_23():
    """Bài 23. Nhiều truy vấn đường đi ngắn nhất (Thảo luận chiến lược tối ưu).""" [cite: 143, 144]
    print("[Bài 23] Chiến lược xử lý nhiều truy vấn đường đi ngắn nhất:")
    print("  - Nếu số truy vấn Q nhỏ: Chạy thuật toán Dijkstra độc lập trực tiếp trên mỗi truy vấn.") [cite: 144, 145]
    print("  - Nếu số truy vấn Q lớn: Thực hiện tiền xử lý tính trước đường đi (ví dụ chạy Dijkstra từ mọi nguồn hoặc Floyd-Warshall) để lưu bộ nhớ đệm giúp trả lời mỗi truy vấn với chi phí O(1).") [cite: 144]


