a = list(map(int, input().split()))
k = int(input())
x = int(input())

left, right = 0, len(a) - k

while left < right:
    mid = (left + right) // 2

    if x - a[mid] > a[mid + k] - x:
        left = mid + 1
    else:
        right = mid

print(*a[left:left + k])