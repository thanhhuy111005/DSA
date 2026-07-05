def cau_33():
    print("\n--- Câu 33. Xoay mảng k vị trí ---")
    a = [1, 2, 3, 4, 5]
    k = 2
    print(f"Mảng gốc: {a}, k = {k}")

    def rotate_inplace(arr, steps):
        n = len(arr)
        steps %= n

        def reverse(l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        # Kỹ thuật đảo mảng thần thánh 3 lần liên tiếp
        reverse(0, n - 1)
        reverse(0, steps - 1)
        reverse(steps, n - 1)

    rotate_inplace(a, k)
    print(f"Mảng sau khi xoay phải {k} vị trí: {a}")
