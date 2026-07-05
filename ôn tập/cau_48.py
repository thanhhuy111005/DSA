def cau_48():
    print("\n--- Câu 48. Rabin-Karp ---")

    def rabin_karp_search(text, pattern):
        n, m = len(text), len(pattern)
        p, mod = 31, 10**9 + 7
        p_pow = 1
        for _ in range(m - 1):
            p_pow = (p_pow * p) % mod

        pat_h = 0
        win_h = 0
        for i in range(m):
            pat_h = (pat_h * p + ord(pattern[i])) % mod
            win_h = (win_h * p + ord(text[i])) % mod

        for i in range(n - m + 1):
            if pat_h == win_h and text[i : i + m] == pattern:
                return i
            if i < n - m:
                # Cập nhật hash cửa sổ trượt thần tốc trong O(1)
                win_h = (win_h - ord(text[i]) * p_pow) % mod
                win_h = (win_h * p + ord(text[i + m])) % mod
                win_h = (win_h + mod) % mod
        return -1

    print(f"Tìm 'abc' trong văn bản 'zabcd' -> Vị trí: {rabin_karp_search('zabcd', 'abc')}")
