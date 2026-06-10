import random

def bubble_sort(a):
    n = len(a)

    compare = 0
    swap = 0

    for i in range(n - 1):
        hoan_doi = False

        for j in range(0, n - i - 1):
            compare += 1

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swap += 1
                hoan_doi = True

        if hoan_doi == False:
            break

    return compare, swap


n = 10

random_array = random.sample(range(1, 100), n)

sorted_array = list(range(1, n + 1))

reverse_array = list(range(n, 0, -1))


c1, s1 = bubble_sort(random_array.copy())
c2, s2 = bubble_sort(sorted_array.copy())
c3, s3 = bubble_sort(reverse_array.copy())

print("Ngẫu nhiên:")
print("So sánh =", c1)
print("Swap =", s1)

print()

print("Đã sắp xếp:")
print("So sánh =", c2)
print("Swap =", s2)

print()

print("Sắp xếp ngược:")
print("So sánh =", c3)
print("Swap =", s3)