weights = list(map(int, input().split()))
days = int(input())

left, right = max(weights), sum(weights)

while left < right:
    mid = (left + right) // 2

    need = 1
    cur = 0

    for w in weights:
        if cur + w > mid:
            need += 1
            cur = 0
        cur += w

    if need <= days:
        right = mid
    else:
        left = mid + 1

print(left)