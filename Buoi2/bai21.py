nums = list(map(int, input().split()))
k = int(input())

left = max(nums)
right = sum(nums)

while left < right:
    mid = (left + right) // 2

    count = 1
    cur = 0

    for num in nums:
        if cur + num > mid:
            count += 1
            cur = num
        else:
            cur += num

    if count <= k:
        right = mid
    else:
        left = mid + 1

print(left)