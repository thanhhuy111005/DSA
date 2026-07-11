def can_split(weights, k, capacity):
    trucks = 1
    current = 0

    for w in weights:
        if current + w <= capacity:
            current += w
        else:
            trucks += 1
            current = w

    return trucks <= k


def min_capacity(weights, k):
    left = max(weights)
    right = sum(weights)

    while left < right:
        mid = (left + right) // 2

        if can_split(weights, k, mid):
            right = mid
        else:
            left = mid + 1

    return left


weights = [1,2,3,4,5,6,7,8,9,10]
k = 5

answer = min_capacity(weights, k)

print("Tải trọng nhỏ nhất:", answer)