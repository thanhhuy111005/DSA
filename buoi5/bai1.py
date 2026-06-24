def bai_1():
    """Bài 1. Biểu diễn đồ thị có trọng số G1 dưới dạng danh sách kề.""" [cite: 2, 3]
    # In ra cấu trúc danh sách kề của đồ thị G1 đã khai báo ở trên
    print("[Bài 1] Danh sách kề (Adjacency List) của đồ thị G1:")
    for u, edges in graph_G1.items():
        print(f"  adj[{u}] = {edges}")


