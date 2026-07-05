# Bài 20. Tìm front và rear [cite: 70, 71]
def bai20(q_list):
    if not q_list: return None, None
    return q_list[0], q_list[-1]

