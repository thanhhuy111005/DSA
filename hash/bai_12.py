def bai_12():
    print("\n--- Bài 12. Tổng đoạn con bằng k ---")
    arr = [1, 1, 1]
    k = 2
    print(f"Mảng: {arr}, k = {k}")

    prefix_counts = {0: 1}  # Base case phục vụ tính tổng tiền tố gốc ban đầu
    current_sum = 0
    total_segments = 0

    for num in arr:
        current_sum += num
        if current_sum - k in prefix_counts:
            total_segments += prefix_counts[current_sum - k]
        prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

    print(f"Số lượng đoạn con liên tiếp có tổng bằng {k} là: {total_segments}")
