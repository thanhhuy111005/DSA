def bai_3():
    print("\n--- Bài 3: Chèn / xóa ở vị trí bất kỳ ---")
    arr = [1, 2, 4]
    print(f"Mảng ban đầu: {arr}")

    # Chèn phần tử 3 tại index 2
    idx_chen = 2
    val_chen = 3
    arr.insert(idx_chen, val_chen)  # O(n) do dịch chuyển các phần tử phía sau
    print(f"Sau khi chèn {val_chen} tại index {idx_chen}: {arr}")

    # Xóa phần tử tại index 1
    idx_xoa = 1
    val_xoa = arr.pop(idx_xoa)  # O(n) do dịch chuyển phần tử lên trước
    print(f"Sau khi xóa tại index {idx_xoa} (giá trị {val_xoa}): {arr}")
