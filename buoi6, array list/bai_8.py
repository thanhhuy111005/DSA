def bai_8():
    print("\n--- Bài 8: Xóa các phần tử thỏa điều kiện ---")
    arr = [1, 2, 3, 4]
    print(f"Mảng gốc: {arr}")

    # Áp dụng kỹ thuật 2 con trỏ (Đọc/Ghi) để tối ưu O(n) thời gian và O(1) bộ nhớ tại chỗ
    write_ptr = 0
    for read_ptr in range(len(arr)):
        # Điều kiện giữ lại: Không phải số chẵn (tức là xóa số chẵn)
        if arr[read_ptr] % 2 != 0:
            arr[write_ptr] = arr[read_ptr]
            write_ptr += 1

    # Cắt tỉa các phần tử thừa phía sau con trỏ ghi
    del arr[write_ptr:]
    print(f"Mảng sau khi xóa các số chẵn (giữ nguyên thứ tự): {arr}")
