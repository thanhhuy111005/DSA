def bai_44(a):
    """Cài đặt Gnome sort - biến thể đơn giản của insertion sort dùng một con trỏ tiến/lùi[cite: 163, 164]."""
    pos = 0
    while pos < len(a):
        if pos == 0 or a[pos] >= a[pos - 1]:
            pos += 1
        else:
            a[pos], a[pos - 1] = a[pos - 1], a[pos]
            pos -= 1
    return a

