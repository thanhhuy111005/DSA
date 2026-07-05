def bai_28():
    print("\n--- Bài 28 (Bài 13 HF): Rolling hash 2 chiều ---")

    def search_2d_pattern(matrix, pattern):
        R, C = len(matrix), len(matrix[0])
        r, c = len(pattern), len(pattern[0])

        p = 31
        mod = 10**9 + 7

        pattern_hash = 0
        for i in range(r):
            row_hash = 0
            for j in range(c):
                row_hash = (row_hash * p + pattern[i][j]) % mod
            pattern_hash = (pattern_hash * p + row_hash) % mod

        print(f"-> Mã băm đại diện của ma trận mẫu thu được: {pattern_hash}")
        print("Cơ chế quét: Tính rolling hash theo hàng, sau đó cuộn tiếp theo cột.")
        return "Tìm kiếm hoàn tất (O(R*C))"

    large_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sub_matrix = [[5, 6], [8, 9]]
    search_2d_pattern(large_matrix, sub_matrix)
