def bai_7():
    print("\n--- Bài 7: Phân tích amortized của append ---")
    print("[Giải thích toán học]:")
    print(
        "- Đa số các lần append chỉ tốn chi phí thực tế là O(1) khi mảng còn chỗ trống."
    )
    print(
        "- Khi mảng đầy ở kích thước N, ta cần tốn O(N) để copy sang mảng mới dung lượng 2N."
    )
    print(
        "- Tổng chi phí cho N lần append liên tiếp: O(1) * N + [1 + 2 + 4 + ... + N] = O(N)."
    )
    print(
        "- Chia trung bình: O(N) / N = O(1). Do đó chi phí thế toán (Amortized Cost) là O(1)."
    )
