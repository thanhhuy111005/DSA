def bai_9():
    print("\n--- Bài 9: Đảo ngược tại chỗ ---")
    arr = [1, 2, 3, 4]
    print(f"Mảng ban đầu: {arr}")

    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]  # Hoán vị hai đầu
        left += 1
        right -= 1

    print(f"Mảng sau khi đảo ngược tại chỗ: {arr}")
