def sentinel_search(a, x):

    n = len(a)

    a.append(x)

    i = 0

    while a[i] != x:
        i += 1

    a.pop()

    if i < n:
        return i

    return -1


a = [7, 3, 9, 12, 5]

x = int(input("Nhap x: "))

print(sentinel_search(a, x))