def first_occurrence(a, x):
    left, right = 0, len(a) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == x:
            ans = mid
            right = mid - 1
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return ans

def last_occurrence(a, x):
    left, right = 0, len(a) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == x:
            ans = mid
            left = mid + 1
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return ans

a = list(map(int, input().split()))
x = int(input())

f = first_occurrence(a, x)

if f == -1:
    print(0)
else:
    l = last_occurrence(a, x)
    print(l - f + 1)