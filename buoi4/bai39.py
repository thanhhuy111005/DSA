def bai_39(students):
    """Sắp danh sách học sinh theo điểm giảm dần, nếu bằng điểm thì theo tên tăng dần[cite: 144, 145]."""
    for i in range(1, len(students)):
        key = students[i]
        j = i - 1
        while j >= 0:
            if students[j][1] < key[1]:
                students[j + 1] = students[j]
                j -= 1
            elif students[j][1] == key[1] and students[j][0] > key[0]:
                students[j + 1] = students[j]
                j -= 1
            else:
                break
        students[j + 1] = key
    return students

