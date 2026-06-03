def integer_sqrt(n):
    left, right = 0, n
    ans = 0

    while left <= right:
        mid = (left + right) // 2

        if mid * mid <= n:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans

n = int(input())
print(integer_sqrt(n))