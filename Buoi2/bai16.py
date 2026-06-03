import math

piles = list(map(int, input().split()))
h = int(input())

left, right = 1, max(piles)

while left < right:
    mid = (left + right) // 2

    hours = 0
    for p in piles:
        hours += math.ceil(p / mid)

    if hours <= h:
        right = mid
    else:
        left = mid + 1

print(left)