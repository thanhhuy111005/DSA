def bai_11():
    print("\n--- Bài 11: Xoay mảng k vị trí ---")
    arr = [1, 2, 3, 4, 5]
    k = 2
    print(f"Mảng ban đầu: {arr}, k = {k}")

    n = len(arr)
    k %= n  # Tránh tràn vòng nếu k > n

    def reverse_helper(l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    # Thuật toán đảo 3 lần đạt O(n) thời gian và O(1) bộ nhớ tại chỗ
    if k > 0:
        reverse_helper(0, n - 1)  # Đảo toàn mảng: [5, 4, 3, 2, 1]
        reverse_helper(0, k - 1)  # Đảo k phần tử đầu: [4, 5, 3, 2, 1]
        reverse_helper(k, n - 1)  # Đảo phần còn lại: [4, 5, 1, 2, 3]

    print(f"Mảng sau khi xoay phải {k} vị trí: {arr}")
