def cau_7():
    print("\n--- Câu 7. Bubble sort & số swap ---")
    a = [2, 3, 1]
    print(f"Mảng gốc: {a}")

    def bubble_sort_count(arr):
        nums = list(arr)
        n = len(nums)
        swap_count = 0
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swap_count += 1
        return nums, swap_count

    sorted_arr, swaps = bubble_sort_count(a)
    print(f"Mảng sau khi xếp: {sorted_arr} | Số lần hoán đổi (Swaps): {swaps}")
    print("Giải thích: Mỗi lần hoán đổi (swap) hai phần tử kề nhau bị ngược thứ tự")
    print("sẽ làm giảm chính xác 1 nghịch thế của mảng. Do đó tổng số swap luôn bằng số cặp nghịch thế ban đầu.")
