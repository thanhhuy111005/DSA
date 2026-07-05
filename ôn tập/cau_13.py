def cau_13():
    print("\n--- Câu 13. Đếm nghịch thế O(n log n) ---")
    a = [1, 3, 5, 2, 4, 6]
    print(f"Mảng: {a}")

    def merge_and_count(arr, l, m, r):
        left = arr[l : m + 1]
        right = arr[m + 1 : r + 1]
        i = j = 0
        k = l
        inv_count = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                # Nếu phần tử bên phải nhỏ hơn, toàn bộ phần tử còn lại của mảng trái đều tạo nghịch thế
                inv_count += (m + 1) - (l + i)
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        return inv_count

    def merge_sort_and_count(arr, l, r):
        inv_count = 0
        if l < r:
            m = (l + r) // 2
            inv_count += merge_sort_and_count(arr, l, m)
            inv_count += merge_sort_and_count(arr, m + 1, r)
            inv_count += merge_and_count(arr, l, m, r)
        return inv_count

    total_inv = merge_sort_and_count(list(a), 0, len(a) - 1)
    print(f"-> Tổng số cặp nghịch thế đếm được bằng Merge Sort: {total_inv}")
