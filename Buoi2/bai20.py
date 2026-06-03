pages = list(map(int, input().split()))
m = int(input())

left = max(pages)
right = sum(pages)

ans = right

while left <= right:
    mid = (left + right) // 2

    students = 1
    cur = 0

    for p in pages:
        if cur + p > mid:
            students += 1
            cur = p
        else:
            cur += p

    if students <= m:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)