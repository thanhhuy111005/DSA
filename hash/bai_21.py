def bai_21():
    print("\n--- Bài 21 (Bài 6 HF): Rolling hash & Rabin-Karp ---")

    def rabin_karp(text, pattern):
        n, m = len(text), len(pattern)
        if m > n:
            return -1

        p = 31
        mod = 10**9 + 7

        # Tính lũy thừa phục vụ loại bỏ ký tự đầu cửa sổ cuốn: p^(m-1)
        p_pow = 1
        for _ in range(m - 1):
            p_pow = (p_pow * p) % mod

        pattern_hash = 0
        current_window_hash = 0

        # Khởi tạo hash ban đầu
        for i in range(m):
            pattern_hash = (pattern_hash * p + ord(pattern[i])) % mod
            current_window_hash = (
                current_window_hash * p + ord(text[i])
            ) % mod

        # Cuộn cửa sổ kiểm tra quét văn bản
        for i in range(n - m + 1):
            if pattern_hash == current_window_hash:
                if text[i : i + m] == pattern:  # Double check tránh trùng mã băm
                    return i

            if i < n - m:
                # Công thức cập nhật Rolling Hash trong O(1) tại chỗ
                current_window_hash = (
                    current_window_hash - ord(text[i]) * p_pow
                ) % mod
                current_window_hash = (
                    current_window_hash * p + ord(text[i + m])
                ) % mod
                current_window_hash = (current_window_hash + mod) % mod

        return -1

    txt = "zabcd"
    pat = "abc"
    print(f"Văn bản: '{txt}' | Mẫu tìm kiếm: '{pat}'")
    print(f"Vị trí tìm thấy mẫu: {rabin_karp(txt, pat)}")
