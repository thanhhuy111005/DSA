def cau_32():
    print("\n--- Câu 32. removeIf tại chỗ ---")
    a = [1, 2, 3, 4]
    print(f"Mảng ban đầu: {a}")

    # Kỹ thuật hai con trỏ tối ưu O(n) thời gian và O(1) không gian lưu trữ
    write_ptr = 0
    for read_ptr in range(len(a)):
        if a[read_ptr] % 2 != 0:  # Điều kiện giữ lại: Số lẻ (tức là xóa số chẵn)
            a[write_ptr] = a[read_ptr]
            write_ptr += 1
    del a[write_ptr:]

    print(f"Mảng sau khi xóa toàn bộ số chẵn tại chỗ: {a}")
