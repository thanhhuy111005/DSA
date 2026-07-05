def cau_31():
    print("\n--- Câu 31. Mở rộng & amortized O(1) ---")
    print("[Phân tích cấu trúc toán học]:")
    print("- Chi phí cho một lượt resizing bộ nhớ mảng từ kích thước N lên 2N là O(N).")
    print("- Tuy nhiên, thao tác này cực kỳ hiếm hoi. Ta chỉ gặp lại nó sau N lần append an nhàn kế tiếp.")
    print("- Tổng chi phí tích lũy qua N phần tử: N * O(1) + O(N) = O(N).")
    print("- Chia trung bình cho N lần: O(N) / N = O(1). Do đó chi phí Amortized đạt O(1).")
