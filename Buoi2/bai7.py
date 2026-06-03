def upper_bound(a, x):
    left, right = 0, len(a)

    while left < right:
        mid = (left + right) // 2

        if a[mid] <= x:
            left = mid + 1
        else:
            right = mid

    return left

a = list(map(int, input().split()))
x = int(input())
print(upper_bound(a, x))