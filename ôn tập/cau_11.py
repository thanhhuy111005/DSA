def cau_11():
    print("\n--- Câu 11. Selection sort & số so sánh ---")
    a = [5, 4, 3, 2, 1]

    def selection_sort_count(arr):
        nums = list(arr)
        n = len(nums)
        comparison_count = 0
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                comparison_count += 1
                if nums[j] < nums[min_idx]:
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
        return comparison_count

    n = len(a)
    comp = selection_sort_count(a)
    print(f"Số lượng phần tử n = {n} -> Số phép so sánh thực tế: {comp}")
    print(f"Theo công thức toán học n*(n-1)/2 = {int(n*(n-1)/2)}")
    print("Chứng minh: Selection sort luôn phải duyệt cạn để tìm min trên đoạn còn lại, nên không có Best Case.")
