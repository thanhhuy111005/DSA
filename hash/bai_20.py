def bai_20():
    print("\n--- Bài 20 (Bài 5 HF): Vì sao chọn m là số nguyên tố ---")
    # Minh chứng thực nghiệm: băm các số chia hết cho 4
    keys = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]

    m_composite = 16  # Luỹ thừa của 2
    m_prime = 17  # Số nguyên tố

    dist_composite = [0] * m_composite
    dist_prime = [0] * m_prime

    for k in keys:
        dist_composite[k % m_composite] += 1
        dist_prime[k % m_prime] += 1

    print(f"Khi m = 16 (Lũy thừa của 2): Các ô được điền là {dist_composite}")
    print("-> Nhược điểm: Bị gom cụm nghiêm trọng vào các ô chia hết cho 4.")
    print(f"Khi m = 17 (Số nguyên tố): Các ô được điền là {dist_prime}")
    print("-> Ưu điểm: Phân bố rải đều, tận dụng tối đa không gian lưu trữ.")
