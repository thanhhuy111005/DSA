def cau_9():
    print("\n--- Câu 9. Insertion sort & số shift ---")
    a = [3, 2, 1]
    print(f"Mảng gốc: {a}")

    def insertion_sort_count(arr):
        nums = list(arr)
        total_shifts = 0
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]  # Thực hiện dịch chuyển phần tử ra sau
                j -= 1
                total_shifts += 1
            nums[j + 1] = key
        return nums, total_shifts

    sorted_arr, shifts = insertion_sort_count(a)
    print(f"Mảng sau khi xếp: {sorted_arr} | Tổng số lần dịch chuyển (Shifts): {shifts}")
    print("Kết luận: Tổng số lần dịch chuyển (shift) phản ánh chính xác số cặp nghịch thế trong mảng.")
