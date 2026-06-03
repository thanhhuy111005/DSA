def find_min(a):
    left, right = 0, len(a) - 1

    while left < right:
        mid = (left + right) // 2

        if a[mid] > a[right]:
            left = mid + 1
        else:
            right = mid

    return a[left]

a = list(map(int, input().split()))
print(find_min(a))