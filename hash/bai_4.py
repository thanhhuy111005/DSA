def bai_4():
    print("\n--- Bài 4. Hai mảng có phần tử chung ---")
    arr1 = [1, 2, 3]
    arr2 = [2, 3, 4]
    print(f"Mảng 1: {arr1} | Mảng 2: {arr2}")

    set1 = set(arr1)
    chung = [x for x in arr2 if x in set1]
    print(f"Các phần tử chung xuất hiện ở cả hai: {chung}")
