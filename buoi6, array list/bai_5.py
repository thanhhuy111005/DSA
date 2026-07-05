def bai_5():
    print("\n--- Bài 5: Duyệt và in phần tử ---")
    arr = [1, 2, 3, 4]
    print(f"Mảng duyệt: {arr}")

    count_chan = 0
    print("Duyệt in từng phần tử: ", end="")
    for x in arr:
        print(x, end=" ")
        if x % 2 == 0:
            count_chan += 1
    print(f"\nSố lượng phần tử thỏa điều kiện (số chẵn): {count_chan}")
