def cau_18():
    print("\n--- Câu 18. Vì sao cần trọng số không âm ---")
    print("Giải thích: Thuật toán Dijkstra dựa trên lòng tin tham lam (Greedy approach). Một khi một đỉnh")
    print("đã được bốc ra khỏi tập xét (chốt đỉnh), khoảng cách tới nó được coi là tối ưu nhất. Nếu đồ thị")
    print("có cạnh mang trọng số âm, một đường đi vòng phía sau có thể làm giảm chi phí xuống nhỏ hơn giá trị")
    print("đã chốt, phá vỡ tính đúng đắn của thuật toán.")
    print("Thuật toán thay thế khi có cạnh âm: Bellman-Ford hoặc thuật toán SPFA.")
