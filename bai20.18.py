def tim_ma_tran(m, x):

    for i in range(len(m)):

        for j in range(len(m[i])):

            if m[i][j] == x:
                return i, j

    return -1, -1


m = [
    [5, 8, 1],
    [3, 9, 7],
    [2, 6, 4]
]

x = 9

print(tim_ma_tran(m, x))