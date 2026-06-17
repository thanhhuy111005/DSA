# bai_50 [Chứng minh tính đúng đắn (loop invariant)]:
# - Bất biến: Trước mỗi vòng lặp ngoài thứ i, đoạn a[0..i-1] chứa đúng các phần tử ban đầu nhưng đã được sắp xếp tăng dần[cite: 188, 189].
# - Khởi tạo (i=1): Đoạn a[0..0] có 1 phần tử, hiển nhiên đúng[cite: 189].
# - Duy trì: Tại vòng thứ i, ta chèn key=a[i] vào đúng vị trí trên đoạn a[0..i-1], giúp đoạn a[0..i] được sắp xếp đúng[cite: 189].
# - Kết thúc: Khi i = n, đoạn a[0..n-1] (toàn mảng) chứa tất cả các phần tử ban đầu và đã được sắp xếp hoàn toàn[cite: 189].