def cau_12():
    print("\n--- Câu 12. So sánh tính ổn định 3 thuật toán ---")
    print("- Bubble Sort: Ổn định (Stable) vì không hoán đổi các phần tử bằng nhau.")
    print("- Insertion Sort: Ổn định (Stable) vì giữ nguyên thứ tự xuất hiện gốc của phần tử bằng nhau.")
    print("- Selection Sort: KHÔNG ổn định (Unstable). Ví dụ phá vỡ thứ tự:")
    print("  Mảng: [ (5, 'A'), (5, 'B'), (1, 'C') ]")
    print("  Lượt đầu tiên tìm được min là 1 ở vị trí cuối, tráo đổi với (5, 'A').")
    print("  Mảng trở thành: [ (1, 'C'), (5, 'B'), (5, 'A') ] -> Thứ tự của 'A' và 'B' đã bị đảo lộn nghịch vị!")
