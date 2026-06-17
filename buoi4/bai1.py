def bai_1(a):
    """Tìm phần tử nhỏ nhất và hoán đổi nó về vị trí đầu tiên[cite: 2, 3]."""
    if not a: return a
    min_idx = 0
    for i in range(1, len(a)):
        if a[i] < a[min_idx]: min_idx = i
    a[0], a[min_idx] = a[min_idx], a[0]
    return a

